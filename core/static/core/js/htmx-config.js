/* ============================================================================
   HTMX-CONFIG.JS - HTMX Configuration
   ============================================================================ */

(function() {
    // Configure HTMX CSRF token
    htmx.config.getCsrfToken = function() {
        return document.querySelector('meta[name="csrf-token"]').content;
    };
    
    // Security: only allow requests to same origin
    htmx.config.selfRequestsOnly = true;
})();
