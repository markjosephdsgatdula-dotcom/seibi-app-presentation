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

  // Slide 4 Dual-Video Setup
  const wiremapVid = document.getElementById('wiremap-video');
  const historyVid = document.getElementById('history-video');
  const videoBadge = document.getElementById('video-badge');

  if (wiremapVid && historyVid) {
    // When the Wire Map video ends, switch to History Log video
    wiremapVid.addEventListener('ended', () => {
      wiremapVid.classList.remove('active');
      historyVid.classList.add('active');
      if (videoBadge) {
        videoBadge.textContent = '履歴ログ';
        videoBadge.classList.add('history-active');
      }
      historyVid.currentTime = 0;
      historyVid.play().catch(err => console.log('Video autoplay blocked:', err));
    });

    // When the History Log video ends, switch back to Wire Map video
    historyVid.addEventListener('ended', () => {
      historyVid.classList.remove('active');
      wiremapVid.classList.add('active');
      if (videoBadge) {
        videoBadge.textContent = 'ワイヤーマップ';
        videoBadge.classList.remove('history-active');
      }
      wiremapVid.currentTime = 0;
      wiremapVid.play().catch(err => console.log('Video autoplay blocked:', err));
    });
  }

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

    // Manage Slide 4 dual-video playback
    if (n === 4) {
      if (wiremapVid && historyVid) {
        wiremapVid.classList.add('active');
        historyVid.classList.remove('active');
        if (videoBadge) {
          videoBadge.textContent = 'ワイヤーマップ';
          videoBadge.classList.remove('history-active');
        }
        wiremapVid.currentTime = 0;
        historyVid.currentTime = 0;
        wiremapVid.play().catch(err => console.log('Video play blocked:', err));
        historyVid.pause();
      }
    } else {
      if (wiremapVid && historyVid) {
        wiremapVid.pause();
        historyVid.pause();
      }
    }
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
