/* ============================================================================
   MOSAIC.JS - Push/Swipe Transition on Hover
   New image enters from the configured direction, pushing current one out.
   ============================================================================ */

(function () {
    const TRANSITION = 'transform 0.75s cubic-bezier(0.4, 0, 0.2, 1)';

    /* Map direction value → CSS translate for entry and exit positions */
    const DIRECTIONS = {
        right:  { entry: 'translateX(100%)',  exit: 'translateX(-100%)' },
        left:   { entry: 'translateX(-100%)', exit: 'translateX(100%)'  },
        top:    { entry: 'translateY(-100%)', exit: 'translateY(100%)'  },
        bottom: { entry: 'translateY(100%)',  exit: 'translateY(-100%)' },
    };

    function setTransform(el, value, animated) {
        el.style.transition = animated ? TRANSITION : 'none';
        el.style.transform  = value;
    }

    function initCell(cell) {
        const images    = Array.from(cell.querySelectorAll('.mosaic-image'));
        if (images.length < 2) return;

        const direction = DIRECTIONS[cell.dataset.direction] || DIRECTIONS.right;
        let currentIdx  = 0;
        let isAnimating = false;

        /* Position all images: first visible, rest off-screen at entry side */
        images.forEach((img, i) => {
            setTransform(img, i === 0 ? 'translateX(0)' : direction.entry, false);
        });

        function advance() {
            if (isAnimating) return;
            isAnimating = true;

            const prevIdx  = currentIdx;
            currentIdx     = (currentIdx + 1) % images.length;

            const prevImg  = images[prevIdx];
            const nextImg  = images[currentIdx];

            /* nextImg is already at entry position (placed there after previous transition) */
            /* Animate both simultaneously */
            setTransform(prevImg, direction.exit,  true);
            setTransform(nextImg, 'translateX(0)', true);

            /* After transition: reset prev to entry position (no animation) for loopback */
            nextImg.addEventListener('transitionend', function onEnd() {
                nextImg.removeEventListener('transitionend', onEnd);
                setTransform(prevImg, direction.entry, false);
                isAnimating = false;
            });
        }

        cell.addEventListener('mouseenter', advance);

        /* Touch support: tap advances to next image */
        let touchMoved = false;
        cell.addEventListener('touchstart', () => { touchMoved = false; }, { passive: true });
        cell.addEventListener('touchmove',  () => { touchMoved = true;  }, { passive: true });
        cell.addEventListener('touchend', () => {
            if (!touchMoved) advance();
        });

        /* Click navigation (if cell has data-link) */
        cell.addEventListener('click', function () {
            const link = this.getAttribute('data-link');
            if (link) window.location.href = link;
        });
    }

    document.querySelectorAll('.mosaic-cell').forEach(initCell);
})();
