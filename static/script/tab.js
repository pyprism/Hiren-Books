/**
 * Created by prism on 10/10/15.
 */
/**
 * function for jquery tab initialization
 */
$(function() {
    $( "#tabs" ).tabs({
        active: 2
    });

    $('#summernote').summernote({height: 200});
});


///**
// * pdfjs
// */
//$( document ).ready(function() {
//    var url = 'http://'  + window.location.host + $('#pdfUrl').text();
//    console.log('http://'  + window.location.host + $('#pdfUrl').text());
//    var pdfDoc = null,
//        pageNum = 2,
//        pageRendering = false,
//        pageNumPending = null,
//        scale = 0.8,
//        canvas = document.getElementById('the-canvas'),
//        ctx = canvas.getContext('2d');
//
//    function renderPage(num) {
//    pageRendering = true;
//    // Using promise to fetch the page
//    pdfDoc.getPage(num).then(function(page) {
//      var viewport = page.getViewport(scale);
//      canvas.height = viewport.height;
//      canvas.width = 900 ;
//
//      // Render PDF page into canvas context
//      var renderContext = {
//        canvasContext: ctx,
//        viewport: viewport
//      };
//      var renderTask = page.render(renderContext);
//
//      // Wait for rendering to finish
//      renderTask.promise.then(function () {
//        pageRendering = false;
//        if (pageNumPending !== null) {
//          // New page rendering is pending
//          renderPage(pageNumPending);
//          pageNumPending = null;
//        }
//      });
//    });
//
//    // Update page counters
//    document.getElementById('page_num').textContent = pageNum;
//  }
//
//  /**
//   * If another page rendering in progress, waits until the rendering is
//   * finised. Otherwise, executes rendering immediately.
//   */
//  function queueRenderPage(num) {
//    if (pageRendering) {
//      pageNumPending = num;
//    } else {
//      renderPage(num);
//    }
//  }
//
//  /**
//   * Displays previous page.
//   */
//  function onPrevPage() {
//    if (pageNum <= 1) {
//      return;
//    }
//    pageNum--;
//    queueRenderPage(pageNum);
//  }
//  document.getElementById('prev').addEventListener('click', onPrevPage);
//
//  /**
//   * Displays next page.
//   */
//  function onNextPage() {
//    if (pageNum >= pdfDoc.numPages) {
//      return;
//    }
//    pageNum++;
//    queueRenderPage(pageNum);
//  }
//  document.getElementById('next').addEventListener('click', onNextPage);
//
//  /**
//   * Asynchronously downloads PDF.
//   */
//  PDFJS.getDocument(url).then(function (pdfDoc_) {
//    pdfDoc = pdfDoc_;
//    document.getElementById('page_count').textContent = pdfDoc.numPages;
//
//    // Initial/first page rendering
//    renderPage(pageNum);
//  });
//
//});
//
///*
//*
// * responsive canvas
//$(document).ready( function(){
//    //Get the canvas &
//    var c = $('#the-canvas');
//    var ct = c.get(0).getContext('2d');
//    var container = $(ct).parent();
//
//    //Run function when browser resizes
//    $(window).resize( respondCanvas );
//
//    function respondCanvas(){
//        c.attr('width', $(container).width() ); //max width
//        c.attr('height', $(container).height() ); //max height
//
//        //Call a function to redraw other content (texts, images etc)
//    }
//
//    //Initial call
//    respondCanvas();
//
//});*/
