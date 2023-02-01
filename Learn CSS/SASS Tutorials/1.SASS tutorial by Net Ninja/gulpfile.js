
const { src, dest, watch, series } = require('gulp')
const sass = require('gulp-sass')(require('sass'))

// create our index.scss to css and dump to a css folder which is destination
function buildStyles(){
    return src('index.scss')
        .pipe(sass())
        .pipe(dest('css'))
}

// watcher function that see the index.scss for any change and if any it 
// recompiles it and again send to css folder   
// watch takes array of files to watch
// second argument is the function that it will run when the file changes
function watchTask(){
    return watch(['index.scss'] , buildStyles)
}

//to run
// series function task argumnent and runs it
exports.default = series(buildStyles,watchTask)