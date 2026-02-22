/* ============================================================================
   LANG.JS - Language Selector
   ============================================================================ */

(function() {
    const langSelect = document.getElementById('language-select');

    if (!langSelect) {
        return;
    }

    // Language change handler
    function changeLanguage(selectElement) {
        const selectedLang = selectElement.value;
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

        window.location.href = newUrl;
    }

    // Attach change event listener (replaces inline onchange)
    langSelect.addEventListener('change', function() {
        changeLanguage(this);
    });

    // Keyboard navigation for language selector
    langSelect.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
            e.preventDefault();
            const options = Array.from(this.options);
            const currentIndex = this.selectedIndex;
            const newIndex = e.key === 'ArrowRight'
                ? (currentIndex + 1) % options.length
                : (currentIndex - 1 + options.length) % options.length;
            this.selectedIndex = newIndex;
            changeLanguage(this);
        }
    });
})();
