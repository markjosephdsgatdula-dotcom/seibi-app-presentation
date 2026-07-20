document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll('.slide');
  const totalSlides = slides.length;
  let currentSlide = 1;

  // DOM Elements
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  const currentSlideNumSpan = document.getElementById('current-slide-num');
  const totalSlidesNumSpan = document.getElementById('total-slides-num');
  const bulletsContainer = document.getElementById('slide-bullets-container');
  const progressBarFill = document.getElementById('progress-bar-fill');

  // Initialize total slide numbers
  totalSlidesNumSpan.textContent = totalSlides;

  // Create bullets dynamically
  for (let i = 1; i <= totalSlides; i++) {
    const bullet = document.createElement('div');
    bullet.classList.add('bullet');
    if (i === 1) bullet.classList.add('active');
    bullet.dataset.slide = i;
    bullet.addEventListener('click', () => {
      goToSlide(i);
    });
    bulletsContainer.appendChild(bullet);
  }

  const bullets = document.querySelectorAll('.bullet');

  // Function to show/change slide
  function goToSlide(n) {
    if (n < 1 || n > totalSlides) return;
    
    // Deactivate current active slide
    const currentActiveSlide = document.querySelector('.slide.active');
    if (currentActiveSlide) {
      currentActiveSlide.classList.remove('active');
    }

    // Activate new slide
    const targetSlide = document.getElementById(`slide-${n}`);
    if (targetSlide) {
      targetSlide.classList.add('active');
    }

    currentSlide = n;
    
    // Update Header Text
    currentSlideNumSpan.textContent = currentSlide;

    // Update Bullets
    bullets.forEach(bullet => {
      if (parseInt(bullet.dataset.slide) === currentSlide) {
        bullet.classList.add('active');
      } else {
        bullet.classList.remove('active');
      }
    });

    // Update Progress Bar
    const progressPercent = (currentSlide / totalSlides) * 100;
    progressBarFill.style.width = `${progressPercent}%`;
  }

  // Next / Prev Button Click handlers
  nextBtn.addEventListener('click', () => {
    if (currentSlide < totalSlides) {
      goToSlide(currentSlide + 1);
    } else {
      // Loop back to start or stay
      goToSlide(1);
    }
  });

  prevBtn.addEventListener('click', () => {
    if (currentSlide > 1) {
      goToSlide(currentSlide - 1);
    } else {
      // Loop to end
      goToSlide(totalSlides);
    }
  });

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
      if (currentSlide < totalSlides) {
        goToSlide(currentSlide + 1);
      } else {
        goToSlide(1);
      }
    } else if (e.key === 'ArrowLeft') {
      e.preventDefault();
      if (currentSlide > 1) {
        goToSlide(currentSlide - 1);
      } else {
        goToSlide(totalSlides);
      }
    }
  });

  // Optional: Click on the slide itself to advance (only if not clicking buttons/links)
  slides.forEach(slide => {
    slide.addEventListener('click', (e) => {
      // Make sure we aren't clicking on a card or button inside the slide
      if (!e.target.closest('.card') && !e.target.closest('.value-card') && !e.target.closest('button')) {
        if (currentSlide < totalSlides) {
          goToSlide(currentSlide + 1);
        } else {
          goToSlide(1);
        }
      }
    });
  });

  // Init Progress Bar on load
  goToSlide(1);
});
