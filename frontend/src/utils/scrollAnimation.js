/**
 * 滚动动画工具
 * 用于处理元素在滚动到视图中时的动画效果
 */

class ScrollAnimation {
  constructor() {
    this.observer = null;
    this.init();
  }

  /**
   * 初始化滚动动画观察器
   */
  init() {
    // 创建Intersection Observer实例
    this.observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // 元素进入视口，添加可见类
          entry.target.classList.add('visible');
          // 一旦元素可见，停止观察
          this.observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1, // 当元素10%进入视口时触发
      rootMargin: '0px 0px -50px 0px' // 底部偏移，提前触发动画
    });

    // 观察所有带有动画类的元素
    this.observeElements();

    // 监听DOM变化，自动观察新添加的元素
    this.observeDOMChanges();
  }

  /**
   * 观察所有带有动画类的元素
   */
  observeElements() {
    const animatedElements = document.querySelectorAll(
      '.fade-in-up, .fade-in-left, .fade-in-right'
    );
    
    animatedElements.forEach(element => {
      this.observer.observe(element);
    });
  }

  /**
   * 监听DOM变化，自动观察新添加的元素
   */
  observeDOMChanges() {
    const observer = new MutationObserver((mutations) => {
      mutations.forEach(mutation => {
        mutation.addedNodes.forEach(node => {
          if (node.nodeType === 1) { // 只处理元素节点
            // 检查节点本身是否带有动画类
            if (node.classList && (
              node.classList.contains('fade-in-up') ||
              node.classList.contains('fade-in-left') ||
              node.classList.contains('fade-in-right')
            )) {
              this.observer.observe(node);
            }
            
            // 检查子节点是否带有动画类
            const animatedChildren = node.querySelectorAll(
              '.fade-in-up, .fade-in-left, .fade-in-right'
            );
            animatedChildren.forEach(child => {
              this.observer.observe(child);
            });
          }
        });
      });
    });

    // 观察整个文档的变化
    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }
}

// 导出单例实例
export default new ScrollAnimation();
