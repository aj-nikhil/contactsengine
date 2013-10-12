$(document).ready(function() {
  $('#content').masonry({
   columnWidth: 320,
   itemSelector: '.item'
  }).imagesLoaded(function() {
   $('#content').masonry('reload');
  });
});

