/* ============================================================================
   TABS.JS - Tab Switching for About Page
   ============================================================================ */

(function() {
    const tabButtons = document.querySelectorAll('.tab-btn');

    if (tabButtons.length === 0) {
        return; // Not on tabs page
    }

    function switchTab(button) {
        const tabId = button.getAttribute('data-tab');
        
        // Remove active from all tabs and panels
        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
        document.querySelectorAll('.tab-panel').forEach(panel => panel.classList.remove('active'));
        
        // Add active to clicked tab and corresponding panel
        button.classList.add('active');
        const panel = document.getElementById(tabId);
        if (panel) {
            panel.classList.add('active');
        }
    }

    // Attach click listeners to all tab buttons
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            switchTab(this);
        });
    });
})();
