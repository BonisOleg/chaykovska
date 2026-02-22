/* ============================================================================
   MOSAIC.JS - Image Rotation with 3s Timer + Slide Effect
   ============================================================================ */

(function() {
    const mosaicCells = document.querySelectorAll('.mosaic-cell');

    if (mosaicCells.length === 0) {
        return; // Not on mosaic page
    }

    // Map to track rotation timers per cell
    const cellTimers = new Map();

    // IntersectionObserver to detect visible cells
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    startCellRotation(entry.target);
                } else {
                    stopCellRotation(entry.target);
                }
            });
        },
        { threshold: 0.5 }
    );

    function startCellRotation(cell) {
        if (cellTimers.has(cell)) {
            return; // Already rotating
        }

        const images = cell.querySelectorAll('.mosaic-image');
        if (images.length === 0) return;

        let currentIndex = 0;

        function rotateImage() {
            const prevIndex = currentIndex;
            currentIndex = (currentIndex + 1) % images.length;

            const prevImage = images[prevIndex];
            const nextImage = images[currentIndex];

            // Remove previous active states
            prevImage.classList.remove('active');

            // Slide effect: current goes left, next comes from right
            prevImage.classList.add('prev');
            nextImage.classList.remove('next');
            nextImage.classList.add('active');

            // After transition, reset slide positions for next rotation
            setTimeout(() => {
                prevImage.classList.remove('prev');
                nextImage.classList.remove('next');
            }, 800);
        }

        // Set random stagger offset (0-1s) for natural feel
        const staggerDelay = Math.random() * 1000;
        const initialTimer = setTimeout(() => {
            rotateImage();
            const timer = setInterval(rotateImage, 3000);
            cellTimers.set(cell, timer);
        }, staggerDelay);

        // Store initial timer too
        cellTimers.set(cell, initialTimer);
    }

    function stopCellRotation(cell) {
        if (cellTimers.has(cell)) {
            clearTimeout(cellTimers.get(cell));
            clearInterval(cellTimers.get(cell));
            cellTimers.delete(cell);
        }
    }

    // Start observing all cells
    mosaicCells.forEach(cell => {
        observer.observe(cell);
        
        // Handle cell clicks (if cell has data-link attribute)
        cell.addEventListener('click', function() {
            const link = this.getAttribute('data-link');
            if (link) {
                window.location.href = link;
            }
        });
    });

    // Cleanup on page unload
    window.addEventListener('unload', () => {
        cellTimers.forEach(timer => {
            clearTimeout(timer);
            clearInterval(timer);
        });
        observer.disconnect();
    });
})();
