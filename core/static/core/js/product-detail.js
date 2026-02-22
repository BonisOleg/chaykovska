/* ============================================================================
   PRODUCT-DETAIL.JS - Product Detail Page Interactions
   ============================================================================ */

(function() {
    const thumbnails = document.querySelectorAll('.thumbnail');
    const mainImage = document.getElementById('main-product-image');
    
    if (thumbnails.length === 0 || !mainImage) return;
    
    thumbnails.forEach(thumb => {
        thumb.addEventListener('click', function() {
            mainImage.src = this.getAttribute('data-full');
        });
    });
})();
