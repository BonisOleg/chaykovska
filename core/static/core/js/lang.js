/* ============================================================================
   LANG.JS - Language Selector (Toggle Buttons)
   ============================================================================ */

(function() {
    const langButtons = document.querySelectorAll('.lang-btn');

    if (langButtons.length === 0) {
        return;
    }

    // Language change handler
    function changeLanguage(selectedLang) {
        const currentUrl = window.location.pathname;

        // Extract current language from URL
        const urlParts = currentUrl.split('/').filter(Boolean);
        const currentLang = urlParts[0];
        const isLangPrefix = ['uk', 'en'].includes(currentLang);

        let newUrl;
        if (isLangPrefix) {
            // Replace language prefix
            newUrl = '/' + selectedLang + '/' + urlParts.slice(1).join('/');
        } else {
            // Add language prefix
            newUrl = '/' + selectedLang + currentUrl;
        }

        // Ensure trailing slash if needed, or keep as is
        window.location.href = newUrl;
    }

    // Attach click event listeners to buttons
    langButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            if (this.classList.contains('lang-btn--active')) {
                return; // Already on this language
            }
            const selectedLang = this.getAttribute('data-lang');
            changeLanguage(selectedLang);
        });
    });
})();
