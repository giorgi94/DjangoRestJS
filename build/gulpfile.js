var path = require("path");
var make_hash = require("./config/hashmaker");

var gulp = require("gulp"),
    gulpif = require("gulp-if"),
    clean = require("gulp-clean"),
    rename = require("gulp-rename"),
    connect = require("gulp-connect");

var imagemin = require("gulp-imagemin"),
    fontmin = require("gulp-fontmin"),
    sourcemaps = require("gulp-sourcemaps"),
    autoprefixer = require("gulp-autoprefixer");
    // babel = require("gulp-babel"),
    // uglify = require("gulp-uglify");


var pug = require("gulp-pug"),
    sass = require("gulp-sass");
    // coffee = require("gulp-coffee");


var PATH = path.join(__dirname, "..");

var NODE_ENV = process.env.NODE_ENV || "development";

var isdev = NODE_ENV === "development";

var use_sourcemaps = isdev,
    use_connect = true;
    // use_uglify = false,
    // use_babel = false;



var abspath = (p) => {
    if(typeof p === "string") {
        return path.join(PATH, p);
    }
    return p.map((val)=>path.join(PATH, val));
};


// Minify

gulp.task("minify/img", () => {
    gulp.src(abspath("assets/img/*"))
        .pipe(imagemin())
        .pipe(gulpif(isdev,
            gulp.dest(abspath("dist/img")),
            gulp.dest(abspath("static/img"))
        ))
        .pipe(gulpif(use_connect, connect.reload()));
});

gulp.task("minify/fonts", () => {
    gulp.src(abspath("assets/fonts/**/*"))
        .pipe(fontmin())
        .pipe(gulpif(isdev,
            gulp.dest(abspath("dist/fonts")),
            gulp.dest(abspath("static/fonts"))
        ))
        .pipe(gulpif(use_connect, connect.reload()));
});

// Pug -> Html

gulp.task("pug", () => {
    gulp.src(abspath("templates/pug/pages/*.pug"))
        .pipe(pug({
            pretty:true
        }).on("error", console.log))
        .pipe(gulp.dest(abspath("templates/jinja2/pages")))
        .pipe(gulpif(use_connect, connect.reload()));
});



// Scripts


gulp.task('js', () => {
    gulp.src(abspath('coffee/*.js'))
        .pipe(gulpif(use_sourcemaps, sourcemaps.init()))
        .pipe(gulpif(use_babel, babel().on('error', console.log)))
        .pipe(gulpif(use_uglify, uglify().on('error', console.log)))
        .pipe(gulpif(use_sourcemaps, sourcemaps.write()))
        .pipe(gulp.dest(abspath('dist/js')))
        .pipe(gulpif(use_connect, connect.reload()));
});

gulp.task('coffee', () => {
    gulp.src(abspath('coffee/*.coffee'))
        .pipe(gulpif(use_sourcemaps, sourcemaps.init()))
        .pipe(coffee().on('error', console.log))
        .pipe(gulpif(use_babel, babel().on('error', console.log)))
        .pipe(gulpif(use_uglify, uglify().on('error', console.log)))
        .pipe(gulpif(use_sourcemaps, sourcemaps.write()))
        .pipe(gulp.dest(abspath('dist/js')))
        .pipe(gulpif(use_connect, connect.reload()));
});


// Styles

gulp.task("sass", () => {

    var hash = isdev ? "" : "-" + make_hash(20, "gulp");

    if(!isdev) {
        gulp.src(abspath("static/css/*"))
            .pipe(clean({force: true}));
    }

    gulp.src(abspath("assets/sass/main.sass"))
        .pipe(rename({
            suffix: hash
        }))
        .pipe(gulpif(use_sourcemaps, sourcemaps.init()))
        .pipe(sass({
            outputStyle: "compressed"
        }).on("error", console.log))
        .pipe(gulpif(use_sourcemaps, sourcemaps.write()))
        .pipe(autoprefixer("last 2 versions", "> 1%", "ie 7"))
        .pipe(gulpif(isdev,
            gulp.dest(abspath("dist/css/")),
            gulp.dest(abspath("static/css/"))
        ))
        .pipe(gulpif(use_connect, connect.reload()));
});



// Main Tasks

gulp.task("build", ["pug", "sass"]);
gulp.task("minify", ["minify/img", "minify/fonts"]);

gulp.task("watch", ()=>{
    gulp.watch(abspath("templates/pug/**/*.pug"), ["pug"]);
    gulp.watch(abspath("assets/sass/**/*.sass"), ["sass"]);

    // gulp.watch(abspath('assets/img/*'), ['minify/img'])
    // gulp.watch(abspath('assets/fonts/*'), ['minify/fonts'])
});

gulp.task("watch/pug", ()=>{
    gulp.watch(abspath("templates/pug/**/*.pug"), ["pug"]);
});



// Server

gulp.task("connect", ()=>{
    connect.server({
        root: abspath([
            "templates/jinja2",
            "dist",
        ]),
        port: 8080,
        livereload: true,
    });
});

gulp.task("server", ["connect", "watch"]);


gulp.task("lr/pug", ["connect", "watch/pug"]);



gulp.task("default", ()=>{
    console.log("hey");
});
