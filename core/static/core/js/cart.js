/* ============================================================================
   CART.JS - HTMX Cart Interactions + Event Re-initialization
   ============================================================================ */

(function() {
    const cartCountEl = document.getElementById('cart-count');

    // Update cart count display
    function updateCartCount(count) {
        if (cartCountEl) {
            cartCountEl.textContent = count;
            if (count === 0 || count === '0') {
                cartCountEl.classList.add('hidden');
            } else {
                cartCountEl.classList.remove('hidden');
            }
        }
    }

    // Re-initialize event listeners on HTMX content swap
    function reinitializeCartEvents() {
        const quantityInputs = document.querySelectorAll('input[name="quantity"]');
        const removeButtons = document.querySelectorAll('.btn-remove');

        quantityInputs.forEach(input => {
            input.addEventListener('change', function(e) {
                e.preventDefault(); // Will be handled by HTMX
            });
        });

        removeButtons.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.preventDefault(); // Will be handled by HTMX
            });
        });

        // Handle product card touch interactions on mobile
        const productCards = document.querySelectorAll('.product-card');
        productCards.forEach(card => {
            card.addEventListener('click', function() {
                if (window.matchMedia('(hover: none)').matches) {
                    this.classList.toggle('active');
                }
            });
        });
    }

    // Listen for HTMX content swaps and re-initialize
    document.addEventListener('htmx:afterSwap', function(evt) {
        // Re-initialize cart events after HTMX swap
        reinitializeCartEvents();

        // Update cart count from response if present
        const cartCount = evt.detail.xhr.getResponseHeader('X-Cart-Count');
        if (cartCount !== null) {
            updateCartCount(cartCount);
        }
    });

    // Initial setup
    document.addEventListener('DOMContentLoaded', function() {
        reinitializeCartEvents();

        // Get initial cart count from element or fetch
        const initialCount = cartCountEl ? cartCountEl.textContent : '0';
        updateCartCount(initialCount);
    });

    // Global function for cart operations (if needed)
    window.updateCartCount = updateCartCount;
})();
