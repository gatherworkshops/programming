/* global module:false */
module.exports = function(grunt) {
	var port = grunt.option('port') || 8000;
	// Project configuration
	grunt.initConfig({

		pkg: grunt.file.readJSON('package.json'),
		

		// SUBTASK: sass theme changes
		sass: {
			main: {
				files: {
					'css/styles.css': 'css/styles.scss'
				}
			}
		},

		// SUBTASK: copy stuff around
		copy: {
			css: {
		    	files: [
		      		{ src: ['_site/css/styles.css'], dest: 'css/styles.css', flatten: true }
		      	]
		    }
		},


		// SUBTASK: build jekyll site
		jekyll: {
			options: {                          // Universal options
		      serve: true,
		      watch: true
		    },
		    dist: {                             // Target
		      options: {                        // Target options
		        dest: '<%= dist %>',
		        config: '_config.yml'
		      }
		    }
		},

		// SUBTASK: watch for changes to auto-run subtasks
		watch: {
			main: {
				files: [ 'Gruntfile.js', 'js/reveal.js', 'css/styles.scss' ],
				tasks: 'default'
			},
			presentation: {
				files: [ '_data/presentation.yml', 'presentation/**/*.md' ],
				tasks: 'jekyll:dist'
			},
			theme: {
				files: [ 'css/*.scss', '_sass/*.scss' ],
				tasks: 'themes'
			}
		}

	});

	// Dependencies
	grunt.loadNpmTasks( 'grunt-jekyll' );
	grunt.loadNpmTasks( 'grunt-contrib-watch' );
	grunt.loadNpmTasks( 'grunt-contrib-sass' );
	grunt.loadNpmTasks( 'grunt-contrib-connect' );
	grunt.loadNpmTasks( 'grunt-contrib-copy' )
	grunt.loadNpmTasks( 'grunt-zip' );

	// Default task
	grunt.registerTask( 'default', [ 'jekyll', 'watch' ] );

	// Serve website locally with change watchers
	//grunt.registerTask( 'watch', [] );

	// Serve website locally
	//grunt.registerTask( 'serve', []);

};
