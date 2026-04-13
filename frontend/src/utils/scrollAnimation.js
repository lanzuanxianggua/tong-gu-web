/**
 * Enhanced Scroll Animation Utility
 * Figma-Inspired Smooth Animations v2.0
 * 
 * Features:
 * - Intersection Observer API for performance
 * - Support for multiple animation types
 * - Staggered animations for lists
 * - Performance optimized with requestAnimationFrame
 */

class ScrollAnimation {
  constructor() {
    this.observer = null;
    this.mutationObserver = null;
    this.animationClasses = [
      'fade-in-up',
      'fade-in-down',
      'fade-in-left',
      'fade-in-right',
      'scale-in',
      'slide-up',
      'slide-down',
      'slide-left',
      'slide-right'
    ];
    
    this.init();
  }

  /**
   * Initialize scroll animation observer with enhanced options
   */
  init() {
    // Create Intersection Observer with refined settings for Figma-like feel
    this.observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry, index) => {
          if (entry.isIntersecting) {
            // Add stagger delay if element has data attribute
            const delay = entry.target.dataset.delay || 0;
            
            setTimeout(() => {
              entry.target.classList.add('visible');
              
              // Trigger custom event for advanced use cases
              entry.target.dispatchEvent(new CustomEvent('animationVisible', {
                bubbles: true,
                detail: { element: entry.target }
              }));
            }, delay);
            
            // Unobserve after animation (one-time trigger)
            if (!entry.target.dataset.repeat) {
              this.observer.unobserve(entry.target);
            }
          } else if (entry.target.dataset.repeat) {
            // Re-trigger animation when scrolling back up (for repeatable animations)
            entry.target.classList.remove('visible');
          }
        });
      },
      {
        threshold: this.getThreshold(),
        rootMargin: '0px 0px -80px 0px'
      }
    );

    // Observe existing elements
    this.observeElements();
    
    // Watch for dynamically added elements
    this.observeDOMChanges();

    // Add global event listeners for enhanced interactions
    this.setupGlobalListeners();
  }

  /**
   * Get dynamic threshold based on screen size for better mobile experience
   */
  getThreshold() {
    if (window.innerWidth < 768) return 0.05; // Lower threshold for mobile
    if (window.innerWidth < 1024) return 0.1;
    return 0.15; // Higher threshold for desktop
  }

  /**
   * Observe all elements with animation classes
   */
  observeElements() {
    const selector = this.animationClasses.join(', ');
    const animatedElements = document.querySelectorAll(selector);
    
    animatedElements.forEach((element, index) => {
      // Add stagger delay if in a list context
      if (element.parentElement?.classList.contains('stagger-children')) {
        const staggerDelay = index * (parseInt(element.parentElement.dataset.stagger) || 100);
        element.dataset.delay = staggerDelay;
      }
      
      this.observer.observe(element);
    });
  }

  /**
   * Monitor DOM changes for dynamically added content (SPA support)
   */
  observeDOMChanges() {
    this.mutationObserver = new MutationObserver((mutations) => {
      // Use requestAnimationFrame to batch DOM updates
      requestAnimationFrame(() => {
        mutations.forEach(mutation => {
          mutation.addedNodes.forEach(node => {
            if (node.nodeType === 1) {
              // Check the node itself
              if (this.hasAnimationClass(node)) {
                this.observer.observe(node);
              }
              
              // Check children recursively
              const children = node.querySelectorAll?.(this.animationClasses.join(', '));
              children?.forEach(child => this.observer.observe(child));
            }
          });
        });
      });
    });

    // Observe document body for changes
    this.mutationObserver.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  /**
   * Check if an element has any animation class
   */
  hasAnimationClass(element) {
    return this.animationClasses.some(cls => element.classList?.contains(cls));
  }

  /**
   * Setup global event listeners for enhanced UX
   */
  setupGlobalListeners() {
    // Handle visibility change (tab switch)
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        // Pause animations when tab is not visible for performance
        document.body.classList.add('animations-paused');
      } else {
        document.body.classList.remove('animations-paused');
      }
    });

    // Optimize for reduced motion preference
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      document.body.classList.add('reduce-motion');
      
      // Immediately show all animated elements
      document.querySelectorAll(this.animationClasses.join(', ')).forEach(el => {
        el.classList.add('visible');
      });
    }

    // Handle resize events to update threshold
    let resizeTimeout;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(() => {
        // Re-observe elements with updated threshold
        this.observer.disconnect();
        this.observeElements();
      }, 250);
    });
  }

  /**
   * Manual trigger - force animation on specific element
   */
  trigger(element) {
    if (element && this.hasAnimationClass(element)) {
      element.classList.add('visible');
      element.dispatchEvent(new CustomEvent('animationVisible', {
        bubbles: true,
        detail: { element }
      }));
    }
  }

  /**
   * Reset animation on element (for re-triggering)
   */
  reset(element) {
    if (element) {
      element.classList.remove('visible');
      // Force reflow
      void element.offsetWidth;
    }
  }

  /**
   * Destroy observer and cleanup
   */
  destroy() {
    if (this.observer) {
      this.observer.disconnect();
    }
    
    if (this.mutationObserver) {
      this.mutationObserver.disconnect();
    }
    
    document.removeEventListener('visibilitychange', this.handleVisibilityChange);
  }
}

// Create and export singleton instance
const scrollAnimation = new ScrollAnimation();

// Expose globally for manual usage
window.ScrollAnimation = scrollAnimation;

export default scrollAnimation;
