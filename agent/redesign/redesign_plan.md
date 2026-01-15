# Complete Trust SoCal Website Redesign

## 1. Complete HTML File (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Trust SoCal - Premier drug and alcohol rehabilitation center in Orange County. Compassionate, evidence-based addiction treatment with 15+ years of experience.">
    <title>Trust SoCal | Drug & Alcohol Rehab Orange County | Insurance Accepted</title>
    <link rel="stylesheet" href="css/styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <!-- Crisis Support Banner -->
    <div class="crisis-banner">
        <div class="container">
            <div class="crisis-content">
                <span class="crisis-text">
                    <i class="fas fa-phone-alt"></i>
                    Crisis Support Available 24/7 - You're Not Alone
                </span>
                <a href="tel:555-123-4567" class="crisis-btn">
                    Call Now: (555) 123-4567
                </a>
            </div>
        </div>
    </div>

    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <img src="images/logo.png" alt="Trust SoCal Logo" class="logo-img">
                    <div class="logo-text">
                        <h1>Trust SoCal</h1>
                        <p class="tagline">Addiction Recovery Center</p>
                    </div>
                </div>
                <nav class="nav">
                    <a href="#services">Treatment Programs</a>
                    <a href="#about">About</a>
                    <a href="#insurance">Insurance</a>
                    <a href="#contact">Contact</a>
                    <a href="tel:555-123-4567" class="btn-call">
                        <i class="fas fa-phone"></i>
                        (555) 123-4567
                    </a>
                </nav>
                <div class="mobile-menu-toggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-background"></div>
        <div class="container">
            <div class="hero-content">
                <div class="hero-text">
                    <h1>Begin Your Healing Journey in Orange County</h1>
                    <p class="hero-subtitle">Compassionate, evidence-based addiction treatment in a peaceful setting. We accept most insurance plans and offer free, confidential assessments 24/7.</p>
                    
                    <div class="hero-stats">
                        <div class="stat">
                            <div class="stat-number">15+</div>
                            <div class="stat-label">Years Experience</div>
                        </div>
                        <div class="stat">
                            <div class="stat-number">7</div>
                            <div class="stat-label">Sober Living Locations</div>
                        </div>
                        <div class="stat">
                            <div class="stat-number">24/7</div>
                            <div class="stat-label">Medical Support</div>
                        </div>
                        <div class="stat">
                            <div class="stat-number">95%</div>
                            <div class="stat-label">Insurance Coverage</div>
                        </div>
                    </div>
                    
                    <div class="hero-buttons">
                        <a href="#insurance" class="btn btn-primary">
                            <i class="fas fa-shield-alt"></i>
                            <span>
                                <strong>Verify Insurance</strong>
                                <small>Free & Confidential</small>
                            </span>
                        </a>
                        <a href="tel:555-123-4567" class="btn btn-secondary">
                            <i class="fas fa-phone"></i>
                            <span>
                                <strong>Call Now</strong>
                                <small>(555) 123-4567</small>
                            </span>
                        </a>
                    </div>
                </div>
                
                <div class="hero-image">
                    <div class="hero-image-container">
                        <img src="images/facility-exterior.jpg" alt="Trust SoCal Peaceful Treatment Facility">
                        <div class="image-badge">
                            <i class="fas fa-star"></i>
                            <span>Premium Facility</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="hero-scroll-indicator">
            <div class="scroll-arrow">
                <i class="fas fa-chevron-down"></i>
            </div>
        </div>
    </section>

    <!-- Trust Signals Section -->
    <section class="trust-signals">
        <div class="container">
            <div class="trust-grid">
                <div class="trust-item">
                    <div class="trust-icon">
                        <i class="fas fa-award"></i>
                    </div>
                    <div class="trust-content">
                        <strong>Joint Commission</strong>
                        <span>Accredited Facility</span>
                    </div>
                </div>
                <div class="trust-item">
                    <div class="trust-icon">
                        <i class="fas fa-certificate"></i>
                    </div>
                    <div class="trust-content">
                        <strong>State Licensed</strong>
                        <span>DHCS Certified</span>
                    </div>
                </div>
                <div class="trust-item">
                    <div class="trust-icon">
                        <div class="rating">
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                        </div>
                    </div>
                    <div class="trust-content">
                        <strong>4.9/5 Rating</strong>
                        <span>Based on 200+ Reviews</span>
                    </div>
                </div>
                <div class="trust-item">
                    <div class="trust-icon">
                        <i class="fas fa-user-shield"></i>
                    </div>
                    <div class="trust-content">
                        <strong>HIPAA Compliant</strong>
                        <span>Your Privacy Protected</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Insurance Verification Section -->
    <section class="insurance-verification" id="insurance">
        <div class="container">
            <div class="verification-content">
                <div class="verification-text">
                    <h2>Check Your Insurance Coverage</h2>
                    <p>Most insurance plans cover addiction treatment. Get verified in under 60 seconds with our confidential online tool.</p>
                    <div class="verification-benefits">
                        <div class="benefit">
                            <i class="fas fa-check-circle"></i>
                            <span>Free, confidential verification</span>
                        </div>
                        <div class="benefit">
                            <i class="fas fa-clock"></i>
                            <span>Instant response within minutes</span>
                        </div>
                        <div class="benefit">
                            <i class="fas fa-dollar-sign"></i>
                            <span>Help maximizing your benefits</span>
                        </div>
                        <div class="benefit">
                            <i class="fas fa-handshake"></i>
                            <span>Direct insurance billing available</span>
                        </div>
                    </div>
                </div>
                <div class="verification-form">
                    <div class="form-container">
                        <h3>Get Started Now</h3>
                        <form class="insurance-form">
                            <div class="form-group">
                                <input type="text" placeholder="Full Name *" required>
                                <i class="fas fa-user"></i>
                            </div>
                            <div class="form-group">
                                <input type="tel" placeholder="Phone Number *" required>
                                <i class="fas fa-phone"></i>
                            </div>
                            <div class="form-group">
                                <input type="email" placeholder="Email Address *" required>
                                <i class="fas fa-envelope"></i>
                            </div>
                            <div class="form-group">
                                <input type="text" placeholder="Insurance Provider *" required>
                                <i class="fas fa-shield-alt"></i>
                            </div>
                            <button type="submit" class="btn btn-primary btn-full">
                                <i class="fas fa-search"></i>
                                Verify My Coverage Now
                            </button>
                        </form>
                        <p class="privacy-note">
                            <i class="fas fa-lock"></i>
                            Your information is 100% confidential and HIPAA protected.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="services">
        <div class="container">
            <div class="section-header">
                <h2>Comprehensive Treatment Programs</h2>
                <p>Evidence-based care at every stage of your recovery journey</p>
            </div>

            <div class="service-grid">
                <!-- Medical Detox -->
                <div class="service-card featured">
                    <div class="service-image">
                        <img src="images/counseling.jpg" alt="Medical Detox Program">
                        <div class="service-badge">Most Popular</div>
                    </div>
                    <div class="service-content">
                        <div class="service-icon">
                            <i class="fas fa-heartbeat"></i>
                        </div>
                        <h3>Medical Detoxification</h3>
                        <p>24/7 medically supervised detoxification with comfort medications and compassionate support to ensure safe, comfortable withdrawal.</p>
                        <ul class="service-features">
                            <li><i class="fas fa-check"></i> 24/7 medical supervision</li>
                            <li><i class="fas fa-check"></i> Comfort medications available</li>
                            <li><i class="fas fa-check"></i> Private rooms with amenities</li>
                            <li><i class="fas fa-check"></i> Nutritional support & meals</li>
                        </ul>
                        <div class="service-cta">
                            <a href="#contact" class="btn btn-outline">Learn More</a>
                        </div>
                    </div>
                </div>

                <!-- Residential Treatment -->
                <div class="service-card featured">
                    <div class="service-image">
                        <img src="images/residential-interior.jpg" alt="Residential Treatment Facility">
                    </div>
                    <div class="service-content">
                        <div class="service-icon">
                            <i class="fas fa-home"></i>
                        </div>
                        <h3>Residential Treatment</h3>
                        <p>30-90 day inpatient programs in comfortable, home-like settings combining therapy, counseling, and holistic treatments.</p>
                        <ul class="service-features">
                            <li><i class="fas fa-check"></i> Private & semi-private rooms</li>
                            <li><i class="fas fa-check"></i> Gourmet meals prepared daily</li>
                            <li><i class="fas fa-check"></i> Individual & group therapy</li>
                            <li><i class="fas fa-check"></i> Recreational activities</li>
                        </ul>
                        <div class="service-cta">
                            <a href="#contact" class="btn btn-outline">Learn More</a>
                        </div>
                    </div>
                </div>

                <!-- PHP -->
                <div class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-calendar-day"></i>
                    </div>
                    <h3>Partial Hospitalization (PHP)</h3>
                    <p>Intensive day treatment allowing you to maintain work and family commitments while receiving comprehensive care.</p>
                    <ul class="service-features">
                        <li><i class="fas fa-check"></i> 6 hours daily, 5 days/week</li>
                        <li><i class="fas fa-check"></i> Individual & group sessions</li>
                        <li><i class="fas fa-check"></i> Family therapy included</li>
                    </ul>
                </div>

                <!-- IOP -->
                <div class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-users"></i>
                    </div>
                    <h3>Intensive Outpatient (IOP)</h3>
                    <p>Flexible evening and weekend programs designed to support your recovery while you rebuild your life.</p>
                    <ul class="service-features">
                        <li><i class="fas fa-check"></i> Evening & weekend options</li>
                        <li><i class="fas fa-check"></i> 3 hours, 3 times per week</li>
                        <li><i class="fas fa-check"></i> Relapse prevention focus</li>
                    </ul>
                </div>

                <!-- Sober Living -->
                <div class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-building"></i>
                    </div>
                    <h3>Sober Living Homes</h3>
                    <p>Seven locations across Southern California providing structured, supportive transitional housing.</p>
                    <ul class="service-features">
                        <li><i class="fas fa-check"></i> 7 locations available</li>
                        <li><i class="fas fa-check"></i> Structured environment</li>
                        <li><i class="fas fa-check"></i> Peer support community</li>
                    </ul>
                </div>

                <!-- Aftercare -->
                <div class="service-card">
                    <div class="service-icon">
                        <i class="fas fa-heart"></i>
                    </div>
                    <h3>Aftercare Support</h3>
                    <p>Ongoing support groups, alumni programs, and resources to help maintain long-term sobriety.</p>
                    <ul class="service-features">
                        <li><i class="fas fa-check"></i> Weekly support groups</li>
                        <li><i class="fas fa-check"></i> Alumni network access</li>
                        <li><i class="fas fa-check"></i> Lifetime support promise</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Facility Showcase -->
    <section class="facility-showcase">
        <div class="container">
            <div class="section-header">
                <h2>Premium Facility & Amenities</h2>
                <p>Experience healing in a comfortable, home-like environment</p>
            </div>
            
            <div class="facility-grid">
                <div class="facility-card">
                    <div class="facility-image">
                        <img src="images/facility-kitchen.jpg" alt="Gourmet Kitchen Facilities">
                    </div>
                    <div class="facility-content">
                        <h3>Gourmet Kitchen</h3>
                        <p>Nutritious, chef-prepared meals to support your physical recovery and wellbeing.</p>
                    </div>
                </div>
                
                <div class="facility-card">
                    <div class="facility-image">
                        <img src="images/facility-bathroom.jpg" alt="Private Bathroom Amenities">
                    </div>
                    <div class="facility-content">
                        <h3>Private Amenities</h3>
                        <p>Comfortable, private spaces designed for relaxation and personal care.</p>
                    </div>
                </div>
                
                <div class="facility-card">
                    <div class="facility-image">
                        <img src="images/meditation-room.jpg" alt="Meditation and Wellness Room">
                    </div>
                    <div class="facility-content">
                        <h3>Wellness Spaces</h3>
                        <p>Dedicated areas for meditation, yoga, and holistic healing practices.</p>
                    </div>
                </div>
                
                <div class="facility-card">
                    <div class="facility-image">
                        <img src="images/therapy-session.jpg" alt="Private Therapy Rooms">
                    </div>
                    <div class="facility-content">
                        <h3>Therapy Rooms</h3>
                        <p>Private, comfortable spaces for individual and group therapy sessions.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <div class="about-content">
                <div class="about-text">
                    <div class="section-header">
                        <h2>Why Choose Trust SoCal?</h2>
                        <p>We've been helping individuals and families overcome addiction in Orange County for over 15 years. Our approach combines medical expertise with genuine compassion.</p>
                    </div>
                    
                    <div class="features-grid">
                        <div class="feature-item">
                            <div class="feature-icon">
                                <i class="fas fa-user-md"></i>
                            </div>
                            <div class="feature-content">
                                <h4>Expert Medical Team</h4>
                                <p>Licensed clinical therapists and medical doctors with 15+ years of addiction treatment experience.</p>
                            </div>
                        </div>
                        
                        <div class="feature-item">
                            <div class="feature-icon">
                                <i class="fas fa-brain"></i>
                            </div>
                            <div class="feature-content">
                                <h4>Evidence-Based Treatment</h4>
                                <p>Proven therapies including CBT, DBT, trauma-informed care, and medication-assisted treatment.</p>
                            </div>
                        </div>
                        
                        <div class="feature-item">
                            <div class="feature-icon">
                                <i class="fas fa-map-marker-alt"></i>
                            </div>
                            <div class="feature-content">
                                <h4>Multiple Locations</h4>
                                <p>7 sober living facilities strategically located across Southern California for convenient access.</p>
                            </div>
                        </div>
                        
                        <div class="feature-item">
                            <div class="feature-icon">
                                <i class="fas fa-users"></i>
                            </div>
                            <div class="feature-content">
                                <h4>Family-Centered Care</h4>
                                <p>We involve families in the recovery process with dedicated family therapy and education programs.</p>
                            </div>
                        </div>
                        
                        <div class="feature-item">
                            <div class="feature-icon">
                                <i class="fas fa-shield-alt"></i>
                            </div>
                            <div class="feature-content">
                                <h4>Insurance Accepted</h4>
                                <p>We work with most major insurance providers and offer financing options to make treatment affordable.</p>
                            </div>
                        </div>
                        
                        <div class="feature-item">
                            <div class="feature-icon">
                                <i class="fas fa-clock"></i>
                            </div>
                            <div class="feature-content">
                                <h4>24/7 Support</h4>
                                <p>Around-the-clock medical supervision and crisis support because recovery doesn't follow business hours.</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="about-image">
                    <img src="images/recovery-path.jpg" alt="Path to Recovery">
                    <div class="about-stats">
                        <div class="stat-box">
                            <div class="stat-number">1000+</div>
                            <div class="stat-label">Lives Changed</div>
                        </div>
                        <div class="stat-box">
                            <div class="stat-number">89%</div>
                            <div class="stat-label">Success Rate</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials">
        <div class="container">
            <div class="section-header">
                <h2>Stories of Hope & Healing</h2>
                <p>Real stories from real people who found their path to recovery</p>
            </div>
            
            <div class="testimonial-grid">
                <div class="testimonial-card">
                    <div class="testimonial-content">
                        <div class="quote-icon">
                            <i class="fas fa-quote-left"></i>
                        </div>
                        <p>"Trust SoCal saved my life. The staff treated me like family, and the facility felt like a peaceful retreat, not a hospital. I've been sober for 2 years now and couldn't be more grateful."</p>
                        <div class="testimonial-author">
                            <div class="author-info">
                                <strong>Michael K.</strong>
                                <span>2 Years Sober</span>
                            </div>
                            <div class="testimonial-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="testimonial-card">
                    <div class="testimonial-content">
                        <div class="quote-icon">
                            <i class="fas fa-quote-left"></i>
                        </div>
                        <p>"The individualized treatment plan and caring staff made all the difference. They helped me address the root causes of my addiction, not just the symptoms. I finally have hope again."</p>
                        <div class="testimonial-author">
                            <div class="author-info">
                                <strong>Sarah M.</strong>
                                <span>18 Months Sober</span>
                            </div>
                            <div class="testimonial-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="testimonial-card">
                    <div class="testimonial-content">
                        <div class="quote-icon">
                            <i class="fas fa-quote-left"></i>
                        </div>
                        <p>"As a parent, watching your child struggle with addiction is heartbreaking. Trust SoCal not only helped my son recover but also gave our entire family the tools to heal together."</p>
                        <div class="testimonial-author">
                            <div class="author-info">
                                <strong>Robert & Linda T.</strong>
                                <span>Family Members</span>
                            </div>
                            <div class="testimonial-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
        <div class="container">
            <div class="cta-content">
                <h2>Ready to Begin Your Recovery Journey?</h2>
                <p>Don't wait another day. Our compassionate team is standing by 24/7 to help you take the first step toward healing.</p>
                <div class="cta-buttons">
                    <a href="tel:555-123-4567" class="btn btn-primary btn-large">
                        <i class="fas fa-phone"></i>
                        Call Now: (555) 123-4567
                    </a>
                    <a href="#insurance" class="btn btn-secondary btn-large">
                        <i class="fas fa-shield-alt"></i>
                        Verify Insurance
                    </a>
                </div>
                <p class="cta-note">
                    <i class="fas fa-lock"></i>
                    All calls and information are completely confidential
                </p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <div class="contact-content">
                <div class="contact-info">
                    <h2>Get Help Today</h2>
                    <p>Reach out now for a free, confidential consultation. We're here to answer your questions and help you understand your treatment options.</p>
                    
                    <div class="contact-methods">
                        <div class="contact-method">
                            <div class="method-icon">
                                <i class="fas fa-phone-alt"></i>
                            </div>
                            <div class="method-content">
                                <h4>Call Us 24/7</h4>
                                <p><a href="tel:555-123-4567">(555) 123-4567</a></p>
                                <small>Immediate support available</small>
                            </div>
                        </div>
                        
                        <div class="contact-method">
                            <div class="method-icon">
                                <i class="fas fa-map-marker-alt"></i>
                            </div>
                            <div class="method-content">
                                <h4>Visit Our Facility</h4>
                                <p>123 Recovery Way<br>Orange County, CA 92618</p>
                                <small>Tours available by appointment</small>
                            </div>
                        </div>
                        
                        <div class="contact-method">
                            <div class="method-icon">
                                <i class="fas fa-envelope"></i>
                            </div>
                            <div class="method-content">
                                <h4>Email Us</h4>
                                <p><a href="mailto:info@trustsocal.com">info@trustsocal.com</a></p>
                                <small>We respond within 2 hours</small>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="contact-form">
                    <h3>Request Information</h3>
                    <form class="main-contact-form">
                        <div class="form-row">
                            <div class="form-group">
                                <input type="text" placeholder="First Name *" required>
                            </div>
                            <div class="form-group">
                                <input type="text" placeholder="Last Name *" required>
                            </div>
                        </div>
                        <div class="form-group">
                            <input type="tel" placeholder="Phone Number *" required>
                        </div>
                        <div class="form-group">
                            <input type="email" placeholder="Email Address *" required>
                        </div>
                        <div class="form-group">
                            <select required>
                                <option value="">Seeking help for...</option>
                                <option value="myself">Myself</option>
                                <option value="family">Family Member</option>
                                <option value="friend">Friend</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <textarea placeholder="Tell us about your situation (optional)" rows="4"></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary btn-full">
                            <i class="fas fa-paper-plane"></i>
                            Send Message
                        </button>
                    </form>
                    <p class="form-privacy">
                        <i class="fas fa-shield-alt"></i>
                        Your information is protected by HIPAA privacy laws
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <div class="footer-logo">
                        <img src="images/logo.png" alt="Trust SoCal Logo">
                        <h3>Trust SoCal</h3>
                    </div>
                    <p>Compassionate addiction treatment in Orange County. We're here to help you reclaim your life from addiction with evidence-based care and genuine support.</p>
                    <div class="footer-social">
                        <a href="#" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="#" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
                
                <div class="footer-section">
                    <h4>Treatment Programs</h4>
                    <ul>
                        <li><a href="#services">Medical Detox</a></li>
                        <li><a href="#services">Residential Treatment</a></li>
                        