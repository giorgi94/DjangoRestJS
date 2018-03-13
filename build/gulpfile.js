var path = require('path');
var make_hash = require('./hash-maker');

var gulp = require('gulp'),
    gulpif = require('gulp-if'),
    clean = require('gulp-clean'),
    rename = require('gulp-rename'),
    connect = require('gulp-connect'),
    livereload = require('gulp-livereload');

var imagemin = require('gulp-imagemin'),
    fontmin = require('gulp-fontmin'),
    sourcemaps = require('gulp-sourcemaps'),
    autoprefixer = require('gulp-autoprefixer');


var pug = require('gulp-pug'),
    sass = require('gulp-sass');
    // coffee = require('gulp-coffee'),
    // babel = require('gulp-babel'),
    // uglify = require('gulp-uglify'),


var PATH = path.join(__dirname, '..')
var NODE_ENV = process.env.NODE_ENV || 'development';

var LIVE_RELOAD = eval(process.env.LIVE_RELOAD || 'false');
var LIVE_SERVER = eval(process.env.LIVE_SERVER || 'false');

var isdev = NODE_ENV === 'development'
var make_sourcemaps = isdev

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
        }))
        .pipe(gulp.dest(abspath('templates/jinja2/')))
        .pipe(gulpif(LIVE_SERVER, connect.reload()))
        .pipe(gulpif(LIVE_RELOAD, livereload()))
});

// Styles

gulp.task('sass', () => {
    var hash = isdev ? '' : '-' + make_hash(20, 'gulp');

    gulp.src(abspath('dist/css/*'))
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
        .pipe(gulpif(LIVE_SERVER, connect.reload()))
        .pipe(gulpif(LIVE_RELOAD, livereload()))
});


// Scripts

// gulp.task('js', () => {
//     gulp.src(abspath('src/js/*.js'))
//         .pipe(gulpif(make_sourcemaps, sourcemaps.init()))
//         .pipe(babel())
//         .pipe(gulpif(make_uglify, uglify()))
//         .pipe(gulpif(make_sourcemaps, sourcemaps.write()))
//         .pipe(gulp.dest(joinpath('dist/js/')))
//         .pipe(gulpif(LIVE_SERVER, connect.reload()))
//         .pipe(gulpif(LIVE_RELOAD, livereload()))
// });


gulp.task('js', () => {
    gulp.src(abspath('src/js/*.js'))
        .pipe(gulpif(LIVE_RELOAD, livereload()))
});



// Server

gulp.task('build', ['pug', 'sass'])
gulp.task('minify', ['minify/img', 'minify/fonts'])

gulp.task('watch', ['build'], ()=>{
    gulp.watch(abspath('templates/pug/**/*.pug'), ['pug'])
    gulp.watch(abspath('assets/**/*.sass'), ['sass'])
})


gulp.task('connect', ()=>{
    connect.server({
        root: abspath([
            'templates/jinja2',
            'dist/',
            'staticfiles/'
        ]),
        port: 8080,
        livereload: true,
    })
})


gulp.task('livereload', ()=>{
    livereload.listen();
    gulp.watch(abspath('assets/**/*.sass'), ['sass'])
    gulp.watch(abspath('templates/pug/**/*.pug'), ['pug'])
    gulp.watch(abspath('src/**/*'), ['js'])
})

gulp.task('default', ['connect', 'watch'])
