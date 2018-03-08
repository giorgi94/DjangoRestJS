const path = require('path');

var gulp = require('gulp'),
    gulpif = require('gulp-if'),
    clean = require('gulp-clean'),
    rename = require('gulp-rename'),
    imagemin = require('gulp-imagemin'),
    fontmin = require('gulp-fontmin'),
    pug = require('gulp-pug'),
    sass = require('gulp-sass'),
    sourcemaps = require('gulp-sourcemaps'),
    autoprefixer = require('gulp-autoprefixer'),
    connect = require('gulp-connect'),
    livereload = require('gulp-livereload');

const { gHash } = require('./hashGenerate');

const NODE_ENV = process.env.NODE_ENV || 'development';
const PATH = path.join(__dirname, '..')

var joinpath = (p) => {
    if(typeof p === 'string') {
        return path.join(PATH, p);
    }
    return p.map((val)=>path.join(PATH, val));
}

var isdev = NODE_ENV === 'development'
var make_sourcemaps = isdev


// Minify

gulp.task('minify/img', () => {
    gulp.src(joinpath('assets/img/**/*'))
        .pipe(imagemin())
        .pipe(gulpif(isdev,
            gulp.dest(joinpath('dist/img')),
            gulp.dest(joinpath('static/img'))
        ))
})

gulp.task('minify/fonts', () => {
    gulp.src(joinpath('assets/fonts/**/*'))
        .pipe(imagemin())
        .pipe(gulpif(isdev,
            gulp.dest(joinpath('dist/fonts')),
            gulp.dest(joinpath('static/fonts'))
        ))
})

gulp.task('minify', ['minify/img', 'minify/fonts'])

// Pug -> Html

gulp.task('pug', () => {
    gulp.src(joinpath('templates/pug/pages/*.pug'))
        .pipe(pug({
            pretty:true
        }))
        .pipe(gulp.dest(joinpath('templates/jinja2')))
        .pipe(connect.reload());
});

// Styles



gulp.task('sass', () => {
    var hash = NODE_ENV === 'development' ? 'dev' : gHash(20, 'gulp');

    gulp.src(joinpath('dist/css/*'))
        .pipe(clean({force: true}))

    gulp.src(joinpath('assets/*.sass'))
        .pipe(rename({
            suffix: `.${hash}`
        }))
        .pipe(gulpif(make_sourcemaps, sourcemaps.init()))
        .pipe(sass({
            outputStyle: 'compressed'
        }).on('error', console.log))
        .pipe(gulpif(make_sourcemaps, sourcemaps.write()))
        .pipe(autoprefixer('last 2 versions', '> 1%', 'ie 7'))
        .pipe(gulpif(isdev,
            gulp.dest(joinpath('dist/css/')),
            gulp.dest(joinpath('static/css/'))
        ))
        .pipe(connect.reload())
});



// Server

gulp.task('build', ['pug', 'sass', 'minify'])

gulp.task('watch', ['build'], ()=>{
    gulp.watch(joinpath('templates/pug/**/*.pug'), ['pug'])
    gulp.watch(joinpath('assets/**/*.sass'), ['sass'])
})


gulp.task('watch/sass', ['sass'], ()=>{
    gulp.watch(joinpath('assets/**/*.sass'), ['sass'])
})

gulp.task('watch/pug', ['pug'], ()=>{
    gulp.watch(joinpath('templates/pug/**/*.pug'), ['pug'])
})


gulp.task('connect', ()=>{
    connect.server({
        root: joinpath([
            'templates/jinja2',
            'dist/',
            'staticfiles/'
        ]),
        port: 8080,
        livereload: true,
    })
})


gulp.task('default', ['connect', 'watch'])
