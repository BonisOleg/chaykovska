/* ============================================================================
   MENU.JS - Fullscreen Navigation Menu Toggle
   ============================================================================ */

(function() {
    const burgerMenu = document.getElementById('burger-menu');
    const navMenu = document.getElementById('nav-menu');
    const closeMenuBtn = document.getElementById('close-menu-btn');
    const body = document.body;

    if (!burgerMenu || !navMenu || !closeMenuBtn) {
        console.warn('Menu elements not found');
        return;
    }

    function toggleMenu() {
        navMenu.classList.toggle('active');
        body.classList.toggle('menu-open');
    }

    function closeMenu() {
        navMenu.classList.remove('active');
        body.classList.remove('menu-open');
    }

    // Open menu on burger click
    burgerMenu.addEventListener('click', toggleMenu);

    // Close menu on close button click
    closeMenuBtn.addEventListener('click', closeMenu);

    // Close menu on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && navMenu.classList.contains('active')) {
            closeMenu();
        }
    });

    // Close menu on nav link click (natural navigation)
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            closeMenu();
        });
    });
})();
