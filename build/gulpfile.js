var path = require('path');
var make_hash = require('./hashmaker');

var gulp = require('gulp'),
    gulpif = require('gulp-if'),
    clean = require('gulp-clean'),
    rename = require('gulp-rename');

var imagemin = require('gulp-imagemin'),
    fontmin = require('gulp-fontmin'),
    sourcemaps = require('gulp-sourcemaps'),
    autoprefixer = require('gulp-autoprefixer');


var pug = require('gulp-pug'),
    sass = require('gulp-sass');


var PATH = path.join(__dirname, '..')
var NODE_ENV = process.env.NODE_ENV || 'development';


var isdev = NODE_ENV === 'development'
var make_sourcemaps = isdev

var hash = isdev ? '' : '-' + make_hash(20, 'gulp');

var abspath = (p) => {
    if(typeof p === 'string') {
        return path.join(PATH, p);
    }
    return p.map((val)=>path.join(PATH, val));
}


// Minify

gulp.task('minify/img', () => {
    gulp.src(abspath('assets/img/**/*'))
        .pipe(imagemin())
        .pipe(gulpif(isdev,
            gulp.dest(abspath('dist/img')),
            gulp.dest(abspath('static/img'))
        ))
})

gulp.task('minify/fonts', () => {
    gulp.src(abspath('assets/fonts/**/*'))
        .pipe(imagemin())
        .pipe(gulpif(isdev,
            gulp.dest(abspath('dist/fonts')),
            gulp.dest(abspath('static/fonts'))
        ))
})

// Pug -> Html

gulp.task('pug', () => {
    gulp.src(abspath('templates/pug/pages/*.pug'))
        .pipe(pug({
            pretty:true
        }).on('error', console.log))
        .pipe(gulp.dest(abspath('templates/jinja2')))
});

// Styles

gulp.task('sass', () => {

    gulp.src(abspath('static/css/*'))
        .pipe(clean({force: true}))

    gulp.src(abspath('assets/*.sass'))
        .pipe(rename({
            suffix: hash
        }))
        .pipe(gulpif(make_sourcemaps, sourcemaps.init()))
        .pipe(sass({
            outputStyle: 'compressed'
        }).on('error', console.log))
        .pipe(gulpif(make_sourcemaps, sourcemaps.write()))
        .pipe(autoprefixer('last 2 versions', '> 1%', 'ie 7'))
        .pipe(gulpif(isdev,
            gulp.dest(abspath('dist/css/')),
            gulp.dest(abspath('static/css/'))
        ))
});


// Server

gulp.task('build', ['pug', 'sass'])
gulp.task('minify', ['minify/img', 'minify/fonts'])

gulp.task('watch', ['build'], ()=>{
    gulp.watch(abspath('templates/pug/**/*.pug'), ['pug'])
    gulp.watch(abspath('assets/**/*.sass'), ['sass'])
})
