// Animations au défilement
document.addEventListener('DOMContentLoaded', function() {
    // Éléments qui s'animeront au scroll
    const animatedElements = document.querySelectorAll('.place-card, .category-card, .promo-section, .testimonial');
    
    // Observer qui détecte quand les éléments entrent dans le viewport
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                // Désinscrire l'élément une fois animé
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    // Observer tous les éléments
    animatedElements.forEach(element => {
        observer.observe(element);
    });
    
    // Slider de vignettes
    const sliders = document.querySelectorAll('.place-image-slider');
    sliders.forEach(slider => {
        const prevBtn = slider.parentElement.querySelector('.slider-prev');
        const nextBtn = slider.parentElement.querySelector('.slider-next');
        const dots = slider.parentElement.querySelectorAll('.dot');
        
        let currentSlide = 0;
        const slides = slider.querySelectorAll('img');
        
        // Fonction pour changer de slide
        function goToSlide(index) {
            currentSlide = index;
            slider.style.transform = `translateX(-${currentSlide * 100}%)`;
            
            // Mettre à jour les dots
            dots.forEach((dot, i) => {
                dot.classList.toggle('active', i === currentSlide);
            });
        }
        
        // Événements des boutons
        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                currentSlide = (currentSlide - 1 + slides.length) % slides.length;
                goToSlide(currentSlide);
            });
        }
        
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                currentSlide = (currentSlide + 1) % slides.length;
                goToSlide(currentSlide);
            });
        }
        
        // Événements des dots
        dots.forEach((dot, i) => {
            dot.addEventListener('click', () => goToSlide(i));
        });
    });
    
    // Effet parallaxe pour le hero
    const hero = document.querySelector('.hero');
    window.addEventListener('scroll', () => {
        const scrollPos = window.scrollY;
        if (hero) {
            const heroVideo = hero.querySelector('.hero-video');
            if (heroVideo) {
                heroVideo.style.transform = `translateY(${scrollPos * 0.3}px)`;
            }
        }
    });
});

// Système de favoris interactif
const favoriteButtons = document.querySelectorAll('.favorite-button');
favoriteButtons.forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        const icon = this.querySelector('i');
        
        // Changer l'icône et ajouter une classe
        if (icon.classList.contains('far')) {
            icon.classList.remove('far');
            icon.classList.add('fas');
            this.classList.add('favorited');
            
            // Animation de battement de cœur
            this.classList.add('pulse-animation');
            setTimeout(() => {
                this.classList.remove('pulse-animation');
            }, 500);
            
            // Notification toast
            showToast('Ajouté aux favoris !');
        } else {
            icon.classList.remove('fas');
            icon.classList.add('far');
            this.classList.remove('favorited');
            showToast('Retiré des favoris');
        }
    });
});

// Système de notification toast
function showToast(message) {
    // Créer un élément de toast s'il n'existe pas
    let toast = document.querySelector('.toast-notification');
    if (!toast) {
        toast = document.createElement('div');
        toast.className = 'toast-notification';
        document.body.appendChild(toast);
    }
    
    // Afficher le message
    toast.textContent = message;
    toast.classList.add('show');
    
    // Masquer après 3 secondes
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Filtres interactifs
const filterTabs = document.querySelectorAll('.filter-tab');
const placeCards = document.querySelectorAll('.place-card');

filterTabs.forEach(tab => {
    tab.addEventListener('click', function() {
        // Retirer la classe active de tous les onglets
        filterTabs.forEach(t => t.classList.remove('active'));
        
        // Ajouter la classe active à l'onglet cliqué
        this.classList.add('active');
        
        const filterType = this.textContent.toLowerCase();
        
        // Filtrer les cartes
        placeCards.forEach(card => {
            if (filterType === 'tous') {
                card.style.display = 'block';
                setTimeout(() => {
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }, 50);
            } else {
                // Vérifier si la carte correspond au filtre
                const isPopular = card.querySelector('.place-card-tag')?.textContent.toLowerCase() === 'populaire';
                const isNew = card.querySelector('.place-card-tag')?.textContent.toLowerCase() === 'nouveau';
                const rating = parseFloat(card.querySelector('.place-rating span')?.textContent || '0');
                const hasPromo = card.querySelector('.old-price') !== null;
                
                let shouldShow = false;
                
                switch(filterType) {
                    case 'populaires':
                        shouldShow = isPopular;
                        break;
                    case 'nouveautés':
                        shouldShow = isNew;
                        break;
                    case 'mieux notés':
                        shouldShow = rating >= 4.5;
                        break;
                    case 'promotions':
                        shouldShow = hasPromo;
                        break;
                }
                
                if (shouldShow) {
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            }
        });
    });
}); 
