// Navigation Drawer Toggle Logic
const hamburgerBtn = document.getElementById('hamburger-btn');
const closeDrawerBtn = document.getElementById('close-drawer-btn');
const navDrawer = document.getElementById('nav-drawer');
const navOverlay = document.getElementById('nav-overlay');
const navLinks = document.querySelectorAll('.nav-list a');

// Open drawer
function openDrawer() {
  navDrawer.classList.add('open');
  navOverlay.classList.add('open');
  hamburgerBtn.classList.add('active');
  document.body.style.overflow = 'hidden';
}

// Close drawer
function closeDrawer() {
  navDrawer.classList.remove('open');
  navOverlay.classList.remove('open');
  hamburgerBtn.classList.remove('active');
  document.body.style.overflow = '';
}

// Toggle drawer
function toggleDrawer() {
  if (navDrawer.classList.contains('open')) {
    closeDrawer();
  } else {
    openDrawer();
  }
}

// Event listeners
hamburgerBtn.addEventListener('click', toggleDrawer);
closeDrawerBtn.addEventListener('click', closeDrawer);
navOverlay.addEventListener('click', closeDrawer);

// Close drawer when a link is clicked
navLinks.forEach(link => {
  link.addEventListener('click', closeDrawer);
});

// Close drawer on escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && navDrawer.classList.contains('open')) {
    closeDrawer();
  }
});
