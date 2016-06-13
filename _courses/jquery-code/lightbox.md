---
layout: default
title: Lightbox
slides:


##########


  - title: title-page
    class: title-slide

    notes: |

      :)

    content: |

      ![Gather Workshops Logo]([[BASE_URL]]/theme/assets/images/gw_logo.png)

      # Lightbox
      _Popup image gallery_


##########


  - title: featherlight
    class: centered-slide

    notes: |

      :)

    content: |

      ## Featherlight

      ![Lightbox Logo](assets/images/lightbox-logo.png)

      Provides a simple way to create a gallery with both thumbnails and full-view images.


  ##########


  - title: download
    class: centered-slide

    notes: |

      :)

    content: |

      ## Download Lightbox

      Download Lightbox from [here](http://lokeshdhakar.com/projects/lightbox2/).

      Unzip the folder once it's downloaded - we'll need to upload some of the files to Neocities!


##########


  - title: zipcontents
    class: centered-slide

    notes: |

      :)

    content: |

      ## What's in the Zip

      There are three folders: css, img, js<br>
      And two files: index.html, README.markdown

      We need to upload just a few of the files:

      - css/lightbox.css
      - js/lightbox.js
      - img/close.png
      - img/next.png
      - img/prev.png
      - img/loading.png


##########


  - title: upload
    class: centered-slide

    notes: |

      :)

    content: |

      ## Upload

      Upload the files to neocities.



##########


  - title: include
    class: centered-slide

    notes: |

      none

    content: |

      ## Include

      Now that we've uploaded the files, we need to tell our HTML page that they exist.

      ```html
      <link rel="stylesheet" href="lightbox.css">
      <script src="lightbox.js"></script>
      ```


##########


  - title: initialise
    class: centered-slide

    notes: |

      :)

    content: |

      ## Initialise Lightbox

      This plugin doesn't need JavaScript initialisation.

      Instead, wrap each image in a link with a data-lightbox attribute.

      ```html
      <a href="image.png" data-lightbox="gallery">
      <img src="image.png">
      </a>
      ```

##########


  - title: summary
    class: centered-slide

    notes: |

      Great! Now that we know the basics, let's get started on our own projects.

    content: |

      ![Thumbs Up!]([[BASE_URL]]/theme/assets/images/thumbs-up.svg){: height="200"}

      ## jQuery Basics: Complete!

      Great, now it's time to build our own...

      [Take me to the next chapter!](slideshow.html)


---







