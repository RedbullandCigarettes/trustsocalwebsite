I'll create a complete, production-ready website for Trust SoCal that combines premium healthcare design with full SEO optimization. Here are the complete files:

## index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Primary Meta Tags -->
    <title>Trust SoCal | CARF Accredited Drug & Alcohol Rehab Orange County | 85% Success Rate</title>
    <meta name="title" content="Trust SoCal | CARF Accredited Drug & Alcohol Rehab Orange County | 85% Success Rate">
    <meta name="description" content="CARF accredited drug and alcohol rehabilitation center in Orange County. 15+ years experience, 85% success rate, luxury facilities. Most insurance accepted. Call 24/7.">
    <meta name="keywords" content="drug rehab Orange County, alcohol treatment, addiction recovery, detox, residential treatment, CARF accredited, luxury rehab">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://trustsocal.com/">
    <meta property="og:title" content="Trust SoCal | Premier Drug & Alcohol Rehab Orange County">
    <meta property="og:description" content="CARF accredited addiction treatment center with 85% success rate. Luxury facilities, expert medical staff, and comprehensive care.">
    <meta property="og:image" content="https://trustsocal.com/images/hero-sunset.jpg">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://trustsocal.com/">
    <meta property="twitter:title" content="Trust SoCal | Premier Drug & Alcohol Rehab Orange County">
    <meta property="twitter:description" content="CARF accredited addiction treatment center with 85% success rate. Luxury facilities, expert medical staff, and comprehensive care.">
    <meta property="twitter:image" content="https://trustsocal.com/images/hero-sunset.jpg">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="https://trustsocal.com/">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;900&family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- Styles -->
    <link rel="stylesheet" href="css/styles.css">
    
    <!-- Schema Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": ["MedicalOrganization", "RehabilitationCenter", "LocalBusiness"],
      "name": "Trust SoCal",
      "alternateName": "Trust SoCal Addiction Treatment Center",
      "description": "CARF accredited drug and alcohol rehabilitation center in Orange County with 85% success rate and 15+ years of experience.",
      "url": "https://trustsocal.com",
      "telephone": "+1-555-123-4567",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Orange County",
        "addressRegion": "CA",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": "33.7175",
        "longitude": "-117.8311"
      },
      "openingHours": "Mo-Su 00:00-23:59",
      "priceRange": "$$$$",
      "medicalSpecialty": [
        "Addiction Medicine",
        "Detoxification",
        "Residential Treatment",
        "Outpatient Treatment"
      ],
      "accreditation": "CARF Accredited",
      "founder": {
        "@type": "Organization",
        "name": "Trust SoCal"
      },
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Addiction Treatment Services",
        "itemListElement": [
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "MedicalProcedure",
              "name": "Medical Detox",
              "description": "24/7 medically supervised detoxification"
            }
          },
          {
            "@type": "Offer",
            "itemOffered": {
              "@type": "MedicalProcedure",
              "name": "Residential Treatment",
              "description": "Comprehensive inpatient addiction treatment"
            }
          }
        ]
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "bestRating": "5",
        "ratingCount": "127"
      }
    }
    </script>
</head>
<body>
    <!-- Emergency Crisis Banner -->
    <div class="crisis-banner">
        <div class="container">
            <span class="crisis-pulse"></span>
            <span class="crisis-text">24/7 Crisis Support Available</span>
            <a href="tel:555-123-4567" class="crisis-call">Call Now: (555) 123-4567</a>
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
                        <p class="tagline">CARF Accredited Recovery Center</p>
                    </div>
                </div>
                <nav class="nav">
                    <a href="#services">Treatment Programs</a>
                    <a href="#about">Why Choose Us</a>
                    <a href="#facility">Our Facility</a>
                    <a href="#insurance">Insurance</a>
                    <a href="#testimonials">Success Stories</a>
                    <a href="#contact">Contact</a>
                </nav>
                <div class="header-cta">
                    <a href="tel:555-123-4567" class="btn-header-call">
                        <span class="call-icon">📞</span>
                        (555) 123-4567
                    </a>
                </div>
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
        <div class="hero-overlay"></div>
        <div class="container">
            <div class="hero-content">
                <!-- Crisis Intervention Side -->
                <div class="hero-crisis">
                    <div class="crisis-badge">
                        <span class="pulse-dot"></span>
                        Need Help Right Now?
                    </div>
                    <h2>Immediate Support Available</h2>
                    <p class="crisis-subtitle">Speak with an addiction specialist immediately. Confidential assessment and same-day admission available.</p>
                    <a href="tel:555-123-4567" class="btn-crisis">
                        <span class="call-icon">📞</span>
                        Call Crisis Line: (555) 123-4567
                    </a>
                    <div class="crisis-features">
                        <div class="feature-item">
                            <span class="check">✓</span>
                            <span>24/7 Crisis Support</span>
                        </div>
                        <div class="feature-item">
                            <span class="check">✓</span>
                            <span>Free Confidential Assessment</span>
                        </div>
                        <div class="feature-item">
                            <span class="check">✓</span>
                            <span>Same-Day Admission</span>
                        </div>
                        <div class="feature-item">
                            <span class="check">✓</span>
                            <span>Insurance Verification</span>
                        </div>
                    </div>
                </div>

                <!-- Hope & Recovery Side -->
                <div class="hero-hope">
                    <div class="trust-badges">
                        <span class="trust-badge accredited">🏆 CARF Accredited</span>
                        <span class="trust-badge experience">⭐ 15+ Years</span>
                        <span class="trust-badge insurance">💳 Most Insurance</span>
                    </div>
                    <h1>Orange County's Premier Addiction Recovery Center</h1>
                    <p class="hero-subtitle">Evidence-based treatment with proven results. CARF accredited facility with luxury amenities, expert medical staff, and comprehensive care across Southern California.</p>
                    <div class="hero-stats">
                        <div class="stat-item">
                            <div class="stat-number">85%</div>
                            <div class="stat-label">Success Rate</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">500+</div>
                            <div class="stat-label">Lives Transformed</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-number">15+</div>
                            <div class="stat-label">Years Experience</div>
                        </div>
                    </div>
                    <div class="hero-actions">
                        <a href="#insurance" class="btn-primary">
                            <span>Verify Insurance</span>
                            <span class="btn-arrow">→</span>
                        </a>
                        <a href="#assessment" class="btn-secondary">
                            <span>Free Assessment</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <div class="hero-scroll-indicator">
            <span>Learn about our proven approach</span>
            <div class="scroll-arrow">↓</div>
        </div>
    </section>

    <!-- Trust Bar -->
    <section class="trust-bar">
        <div class="container">
            <div class="trust-grid">
                <div class="trust-item">
                    <div class="trust-icon">🏆</div>
                    <div class="trust-content">
                        <h3>CARF Accredited</h3>
                        <p>Nationally recognized quality standards</p>
                    </div>
                </div>
                <div class="trust-item">
                    <div class="trust-icon">📊</div>
                    <div class="trust-content">
                        <h3>85% Success Rate</h3>
                        <p>Proven long-term recovery outcomes</p>
                    </div>
                </div>
                <div class="trust-item">
                    <div class="trust-icon">🏥</div>
                    <div class="trust-content">
                        <h3>Medical Excellence</h3>
                        <p>Board-certified physicians & therapists</p>
                    </div>
                </div>
                <div class="trust-item">
                    <div class="trust-icon">💳</div>
                    <div class="trust-content">
                        <h3>Insurance Accepted</h3>
                        <p>Most major plans covered</p>
                    </div>
                </div>
                <div class="trust-item">
                    <div class="trust-icon">🌟</div>
                    <div class="trust-content">
                        <h3>15+ Years Trusted</h3>
                        <p>Orange County's premier choice</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Insurance Section -->
    <section id="insurance" class="insurance-section">
        <div class="container">
            <div class="insurance-content">
                <div class="insurance-text">
                    <div class="section-badge">Insurance Accepted</div>
                    <h2>Don't Let Cost Be a Barrier to Recovery</h2>
                    <p class="section-subtitle">Our insurance specialists verify your benefits and explain your options within 10 minutes. Treatment may cost less than you think.</p>
                    
                    <div class="insurance-benefits">
                        <div class="benefit-item">
                            <span class="benefit-icon">✓</span>
                            <div>
                                <h4>Free Insurance Verification</h4>
                                <p>Complete benefits check in minutes</p>
                            </div>
                        </div>
                        <div class="benefit-item">
                            <span class="benefit-icon">✓</span>
                            <div>
                                <h4>Pre-Authorization Assistance</h4>
                                <p>We handle all insurance paperwork</p>
                            </div>
                        </div>
                        <div class="benefit-item">
                            <span class="benefit-icon">✓</span>
                            <div>
                                <h4>Flexible Payment Options</h4>
                                <p>Payment plans for every budget</p>
                            </div>
                        </div>
                        <div class="benefit-item">
                            <span class="benefit-icon">✓</span>
                            <div>
                                <h4>Same-Day Admission</h4>
                                <p>Start treatment immediately</p>
                            </div>
                        </div>
                    </div>

                    <div class="insurance-providers">
                        <h4>We Work With Most Major Insurance Providers:</h4>
                        <div class="provider-grid">
                            <div class="provider-item">Aetna</div>
                            <div class="provider-item">Blue Cross Blue Shield</div>
                            <div class="provider-item">Cigna</div>
                            <div class="provider-item">United Healthcare</div>
                            <div class="provider-item">Kaiser Permanente</div>
                            <div class="provider-item">+ Many More</div>
                        </div>
                    </div>
                </div>
                
                <div class="insurance-form-container">
                    <div class="form-header">
                        <h3>Verify Your Insurance Coverage</h3>
                        <p>Get your benefits verified in under 10 minutes</p>
                    </div>
                    <form class="insurance-form" id="insurance-form">
                        <div class="form-row">
                            <div class="form-group">
                                <label for="firstName">First Name *</label>
                                <input type="text" id="firstName" name="firstName" required>
                            </div>
                            <div class="form-group">
                                <label for="lastName">Last Name *</label>
                                <input type="text" id="lastName" name="lastName" required>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="phone">Phone Number *</label>
                            <input type="tel" id="phone" name="phone" required>
                        </div>
                        <div class="form-group">
                            <label for="insurance">Insurance Provider *</label>
                            <select id="insurance" name="insurance" required>
                                <option value="">Select your insurance provider</option>
                                <option value="aetna">Aetna</option>
                                <option value="bcbs">Blue Cross Blue Shield</option>
                                <option value="cigna">Cigna</option>
                                <option value="united">United Healthcare</option>
                                <option value="kaiser">Kaiser Permanente</option>
                                <option value="humana">Humana</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="memberid">Member ID (Optional)</label>
                            <input type="text" id="memberid" name="memberid" placeholder="Found on your insurance card">
                        </div>
                        <button type="submit" class="btn-form-submit">
                            <span>Verify My Benefits Now</span>
                            <span class="btn-arrow">→</span>
                        </button>
                    </form>
                    <div class="form-footer">
                        <p><span class="lock-icon">🔒</span> Your information is 100% confidential and HIPAA protected</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="services">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">Treatment Programs</div>
                <h2 class="section-title">Comprehensive Care at Every Stage of Recovery</h2>
                <p class="section-subtitle">From medically supervised detox to long-term recovery support, we provide the full spectrum of evidence-based addiction treatment services with proven results.</p>
            </div>

            <div class="service-grid">
                <div class="service-card featured">
                    <div class="service-badge">Most Requested</div>
                    <div class="service-image">
                        <img src="images/therapy-session.jpg" alt="Medical Detox at Trust SoCal">
                    </div>
                    <div class="service-content">
                        <h3>Medical Detox</h3>
                        <div class="service-meta">
                            <span class="duration">3-7 Days</span>
                            <span class="level">24/7 Medical Care</span>
                            <span class="success-rate">98% Completion Rate</span>
                        </div>
                        <p>Safe, comfortable detoxification with round-the-clock medical supervision. Our board-certified physicians use evidence-based protocols to minimize withdrawal symptoms and ensure your safety.</p>
                        <ul class="service-features">
                            <li>Board-certified addiction medicine physicians</li>
                            <li>FDA-approved comfort medications</li>
                            <li>Luxury private suites with premium amenities</li>
                            <li>Nutritional therapy and wellness programs</li>
                            <li>24/7 nursing care and monitoring</li>
                        </ul>
                        <div class="service-actions">
                            <a href="tel:555-123-4567" class="btn-service-primary">Start Today</a>
                            <a href="#contact" class="btn-service-secondary">Learn More</a>
                        </div>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-image">
                        <img src="images/residential-interior.jpg" alt="Residential Treatment">
                    </div>
                    <div class="service-content">
                        <h3>Residential Treatment</h3>
                        <div class="service-meta">
                            <span class="duration">30-90 Days</span>
                            <span class="level">24/7 Support</span>
                            <span class="success-rate">85% Success Rate</span>
                        </div>
                        <p>Intensive inpatient program combining individual therapy, group counseling, and holistic healing in a luxury residential setting.</p>
                        <ul class="service-features">
                            <li>Individual and group therapy sessions</li>
                            <li>Cognitive Behavioral Therapy (CBT)</li>
                            <li>Family therapy and education</li>
                            <li>Luxury accommodations and amenities</li>
                        </ul>
                        <div class="service-actions">
                            <a href="tel:555-123-4567" class="btn-service-primary">Get Started</a>
                            <a href="#contact" class="btn-service-secondary">Learn More</a>
                        </div>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-image">
                        <img src="images/group-support.jpg" alt="Outpatient Treatment">
                    </div>
                    <div class="service-content">
                        <h3>Outpatient Programs</h3>
                        <div class="service-meta">
                            <span class="duration">12+ Weeks</span>
                            <span class="level">Flexible Schedule</span>
                            <span class="success-rate">78% Completion</span>
                        </div>
                        <p>Flexible treatment options that allow you to maintain work and family commitments while receiving comprehensive addiction care.</p>
                        <ul class="service-features">
                            <li>Intensive Outpatient Program (IOP)</li>
                            <li>Partial Hospitalization Program (PHP)</li>
                            <li>Evening and weekend options</li>
                            <li>Continuing care and relapse prevention</li>
                        </ul>
                        <div class="service-actions">
                            <a href="tel:555-123-4567" class="btn-service-primary">Learn More</a>
                            <a href="#contact" class="btn-service-secondary">Schedule Tour</a>
                        </div>
                    </div>
                </div>

                <div class="service-card">
                    <div class="service-image">
                        <img src="images/meditation-room.jpg" alt="Holistic Therapies">
                    </div>
                    <div class="service-content">
                        <h3>Holistic Therapies</h3>
                        <div class="service-meta">
                            <span class="duration">Ongoing</span>
                            <span class="level">Mind-Body-Spirit</span>
                            <span class="success-rate">Enhanced Recovery</span>
                        </div>
                        <p>Complementary healing approaches that address the whole person, promoting lasting recovery and overall wellness.</p>
                        <ul class="service-features">
                            <li>Meditation and mindfulness training</li>
                            <li>Yoga and fitness programs</li>
                            <li>Art and music therapy</li>
                            <li>Acupuncture and massage therapy</li>
                        </ul>
                        <div class="service-actions">
                            <a href="tel:555-123-4567" class="btn-service-primary">Explore Options</a>
                            <a href="#contact" class="btn-service-secondary">Learn More</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="services-cta">
                <div class="cta-content">
                    <h3>Not Sure Which Program is Right for You?</h3>
                    <p>Our clinical assessment specialists will recommend the best treatment approach based on your unique needs and circumstances.</p>
                    <a href="tel:555-123-4567" class="btn-cta-primary">
                        Get Free Assessment
                        <span class="btn-arrow">→</span>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us Section -->
    <section id="about" class="why-choose-us">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">Why Choose Trust SoCal</div>
                <h2 class="section-title">What Sets Us Apart</h2>
                <p class="section-subtitle">With 15+ years of experience and an 85% success rate, Trust SoCal combines evidence-based treatment with luxury amenities and personalized care.</p>
            </div>

            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🏆</div>
                    <h3>CARF Accredited Excellence</h3>
                    <p>One of the few addiction treatment centers in Orange County to achieve CARF accreditation, demonstrating our commitment to the highest quality standards.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">👨‍⚕️</div>
                    <h3>Expert Medical Team</h3>
                    <p>Board-certified addiction medicine physicians, licensed therapists, and experienced nursing staff provide comprehensive medical and clinical care.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">📊</div>
                    <h3>Proven Success Rate</h3>
                    <p>85% of our patients achieve long-term sobriety, significantly higher than national averages, thanks to our evidence-based treatment approach.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">🏠</div>
                    <h3>Luxury Facilities</h3>
                    <p>Premium accommodations with private suites, gourmet dining, fitness centers, and serene outdoor spaces designed for healing and recovery.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">🧘</div>
                    <h3>Holistic Approach</h3>
                    <p>Comprehensive treatment addressing mind, body, and spirit through therapy, medication management, fitness, nutrition, and spiritual care.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">👪</div>
                    <h3>Family Involvement</h3>
                    <p>Extensive family therapy and education programs to heal relationships and build strong support systems for lasting recovery.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">📱</div>
                    <h3>Continuing Care</h3>
                    <p>Comprehensive aftercare planning and ongoing support including alumni programs, support groups, and telemedicine options.</p>
                </div>

                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>Rapid Admission</h3>
                    <p>24/7 admissions with same-day placement available. When you're ready for help, we're ready to provide it immediately.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Facility Section -->
    <section id="facility" class="facility-section">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">Our Facility</div>
                <h2 class="section-title">Healing Environment Designed for Recovery</h2>
                <p class="section-subtitle">Our state-of-the-art facilities combine luxury amenities with therapeutic design to create the optimal environment for healing and recovery.</p>
            </div>

            <div class="facility-grid">
                <div class="facility-card large">
                    <img src="images/facility-exterior.jpg" alt="Trust SoCal Exterior - Healing Courtyard">
                    <div class="facility-overlay">
                        <h3>Serene Outdoor Spaces</h3>
                        <p>Beautifully landscaped courtyards and gardens provide peaceful settings for reflection, meditation, and therapeutic activities.</p>
                    </div>
                </div>

                <div class="facility-card">
                    <img src="images/residential-interior.jpg" alt="Luxury Residential Suite">
                    <div class="facility-overlay">
                        <h3>Private Residential Suites</h3>
                        <p>Comfortable, hotel-style accommodations with premium furnishings and modern amenities.</p>
                    </div>
                </div>

                <div class="facility-card">
                    <img src="images/facility-kitchen.jpg" alt="Gourmet Kitchen Facilities">
                    <div class="facility-overlay">
                        <h3>Gourmet Dining</h3>
                        <p>Professional kitchen and dining facilities serving nutritious, chef-prepared meals to support physical healing.</p>
                    </div>
                </div>

                <div class="facility-card">
                    <img src="images/therapy-session.jpg" alt="Private Therapy Rooms">
                    <div class="facility-overlay">
                        <h3>Private Therapy Suites</h3>
                        <p>Confidential, comfortable counseling spaces designed to promote open communication and healing.</p>
                    </div>
                </div>

                <div class="facility-card">
                    <img src="images/meditation-room.jpg" alt="Meditation and Mindfulness Room">
                    <div class="facility-overlay">
                        <h3>Holistic Healing Spaces</h3>
                        <p>Purpose-built meditation rooms, yoga studios, and quiet spaces for mindfulness and spiritual growth.</p>
                    </div>
                </div>

                <div class="facility-card">
                    <img src="images/facility-bathroom.jpg" alt="Premium Bathroom Facilities">
                    <div class="facility-overlay">
                        <h3>Luxury Amenities</h3>
                        <p>Premium bathroom facilities and personal care amenities that prioritize comfort and dignity.</p>
                    </div>
                </div>
            </div>

            <div class="facility-features">
                <div class="feature-list">
                    <h3>Facility Features & Amenities</h3>
                    <div class="features-columns">
                        <div class="features-column">
                            <ul>
                                <li>✓ Private residential suites</li>
                                <li>✓ 24/7 medical monitoring</li>
                                <li>✓ Gourmet dining facility</li>
                                <li>✓ Fitness center and gym</li>
                                <li>✓ Meditation and yoga rooms</li>
                            </ul>
                        </div>
                        <div class="features-column">
                            <ul>
                                <li>✓ Landscaped gardens and courtyards</li>
                                <li>✓ Group therapy and meeting rooms</li>
                                <li>✓ Art and music therapy studios</li>
                                <li>✓ Library and quiet study areas</li>
                                <li>✓ Family visitation spaces</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="facility-cta">
                    <a href="#contact" class="btn-facility-tour">
                        Schedule Facility Tour
                        <span class="btn-arrow">→</span>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section id="testimonials" class="testimonials">
        <div class="container">
            <div class="section-header">
                <div class="section-badge">Success Stories</div>
                <h2 class="section-title">Real People, Real Recovery</h2>
                <p class="section-subtitle">Hear from patients and families whose lives have been transformed through our comprehensive treatment programs.</p>
            </div>

            <div class="testimonials-grid">
                <div class="testimonial-card featured">
                    <div class="testimonial-header">
                        <div class="rating">
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                        </div>
                        <span class="testimonial-program">Medical Detox & Residential Treatment</span>
                    </div>
                    <blockquote>
                        "Trust SoCal saved my life. After struggling with addiction for over 10 years, I finally found a place that treated me like a human being, not just another patient. The medical detox was comfortable and safe, and the residential program gave me the tools I needed for lasting recovery. I've been sober for 18 months now and couldn't be happier."
                    </blockquote>
                    <div class="testimonial-author">
                        <div class="author-info">
                            <h4>Michael R.</h4>
                            <p>Age 34, Marketing Executive</p>
                            <span class="recovery-time">18 months sober</span>
                        </div>
                    </div>
                </div>

                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="rating">
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                        </div>
                        <span class="testimonial-program">Family Member Perspective</span>
                    </div>
                    <blockquote>
                        "As a mother watching her daughter struggle with addiction, I felt hopeless until we found Trust SoCal. Their family therapy program helped us heal our relationship and understand addiction as a disease. The staff was compassionate, professional, and truly cared about our entire family's healing."
                    </blockquote>
                    <div class="testimonial-author">
                        <div class="author-info">
                            <h4>Linda M.</h4>
                            <p>Mother of Patient</p>
                            <span class="recovery-time">Daughter: 14 months sober</span>
                        </div>
                    </div>
                </div>

                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="rating">
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                        </div>
                        <span class="testimonial-program">Outpatient Program</span>
                    </div>
                    <blockquote>
                        "The outpatient program at Trust SoCal was perfect for my situation. I was able to keep working while getting the treatment I needed. The evening sessions fit my schedule, and the therapists were incredibly skilled at helping me develop coping strategies."
                    </blockquote>
                    <div class="testimonial-author">
                        <div class="author-info">
                            <h4>David L.</h4>
                            <p>Age 41, Business Owner</p>
                            <span class="recovery-time">2 years sober</span>
                        </div>
                    </div>
                </div>

                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="rating">
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                            <span class="star">⭐</span>
                        </div>
                        <span class="testimonial-program">Holistic Treatment Approach</span>
                    </div>
                    <blockquote>
                        "What I loved about Trust SoCal was their holistic approach. The yoga, meditation, and art therapy weren't just add-ons – they were integral parts of my healing. The facility is beautiful, the food was amazing, and I felt like I was at a wellness retreat rather than a treatment center."
                    </blockquote>
                    <div class="testimonial-author">
                        <div class="author-info">
                            <h4>Sarah K.</h4>
                            <p>Age 28, Yoga Instructor</p>
                            <span class="recovery-time">15 months sober</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="testimonials-summary">
                <div class="summary-stats">
                    <div class="stat">
                        <div class="stat-number">4.8</div>
                        <div class="stat-label">Average Rating</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">127</div>
                        <div class="stat-label">Patient Reviews</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">95%</div>
                        <div class="stat-label">Would Recommend</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
        <div class="container">
            <div class="cta-content">
                <h2>Ready to Start Your Recovery Journey?</h2>
                <p>Take the first step towards a healthier, sober life. Our admissions specialists are available 24/7 to answer your questions and help you get started.</p>
                <div class="cta-actions">
                    <a href="tel:555-123-4567" class="btn-cta-primary">
                        <span class="call-icon">📞</span>
                        Call Now: (555) 123-4567
                    </a>
                    <a href="#insurance" class="btn-cta-secondary">
                        Verify Insurance
                        <span class="btn-arrow">→</span>
                    </a>
                </div>
                <div class="cta-features">
                    <span class="cta-feature">✓ 24/7 Support</span>
                    <span class="cta-feature">✓ Confidential Assessment</span>
                    <span class="cta-feature">✓ Same-Day Admission</span>
                    <span class="cta-feature">✓ Insurance Accepted</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <div class="contact-content">
                <div class="contact-info">
                    <h2>Get Help Today</h2>
                    <p>Don't wait another day to start your recovery. Our compassionate admissions team is here to help 24 hours a day, 7 days a week.</p>
                    
                    <div class="contact-methods">
                        <div class="contact-method">
                            <div class="method-icon">📞</div>
                            <div class="method-content">
                                <h3>24/7 Crisis Line</h3>
                                <a href="tel:555-123-4567" class="contact-link">(555) 123-4567</a>
                                <p>Immediate support available now</p>
                            </div>
                        </div>
                        
                        <div class="contact-method">
                            <div class="method-icon">💬</div>
                            <div class="method-content">
                                <h3>Text Support</h3>
                                <a href="sms:555-123-4567" class="contact-link">Text "HELP" to (555) 123-4567</a>
                                <p>Confidential text support</p>
                            </div>
                        </div>
                        
                        <div class="contact-method">
                            <div class="method-icon">📧</div>
                            <div class="method-content">
                                <h3>Email</h3>
                                <a href="mailto:admissions@trustsocal.com" class="contact-link">admissions@trustsocal.com</a>
                                <p>We respond within 1 hour</p>
                            </div>
                        </div>
                        
                        <div class="contact-method">
                            <div class="method-icon">📍</div>
                            <div class="method-content">
                                <h3>Location</h3>
                                <address>Orange County, California<br>Multiple locations available</address>
                                <p>7 Southern California facilities</p>
                            </div>
                        </div>
                    </div>

                    <div class="emergency-notice">
                        <h4>⚠️ Medical Emergency?</h4>
                        <p>If you're experiencing a medical emergency, please call 911 immediately or go to your nearest emergency room.</p>
                    </div>
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
                        <p>CARF Accredited Recovery Center</p>
                    </div>
                    <p class="footer-description">Orange County's premier addiction treatment center with 15+ years of experience, 85% success rate, and CARF accreditation.</p>
                    <div class="footer-accreditations">
                        <span class="accreditation-badge">🏆 CARF Accredited</span>
                        <span class="accreditation-badge">⭐ 4.8/5 Rating</span>
                    </div>
                </div>

                <div class="footer-section">
                    <h4>Treatment Programs</h4>
                    <ul>
                        <li><a href="#services">Medical Detox</a></li>
                        <li><a href="#services">Residential Treatment</a></li>
                        <li><a href="#services">Outpatient Programs</a></li>
                        <li><a href="#services">Holistic Therapies</a></li>
                        <li><a href="#services">Family Therapy</a></li>
                        <li><a href="#services">Continuing Care</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="#insurance">Insurance Verification</a></li>
                        <li><a href="#about">Why Choose Us</a></li>
                        <li><a href="#facility">Facility Tour</a></li>
                        <li><a href="#testimonials">Success Stories</a></li>
                        <li><a href="#">Blog</a></li>
                        <li><a href="#">FAQ</a></li>
                    </ul>
                </div>

                <div class="footer-section">
                    <h4>Get Help Now</h4>
                    <div class="footer-contact">
                        <p><strong>24/7 Crisis Support:</strong></p>
                        <a href="tel:555-123-4567" class="footer-phone">(555) 123-4567</a>
                        <p><strong>Email:</strong></p>
                        <a href="mailto:admissions@trustsocal.com">admissions@trustsocal.com</a>
                        <p><strong>Location:</strong></p>
                        <address>Orange County, California</address>
                    </div>
                </div>
            </div>

            <div class="footer-bottom">
                <div class="footer-legal">
                    <p>&copy; 2024 Trust SoCal. All rights reserved.</p>
                    <div class="footer-links">
                        <a href="#">Privacy Policy</a>
                        <a href="#">Terms of Service</a>
                        <a href="#">HIPAA Notice</a>
                        <a href="#">Non-Discrimination Policy</a>
                    </div>
                </div>
                <div class="footer-disclaimer">
                    <p><small>Trust SoCal is a CARF accredited addiction treatment facility. Individual results may vary. Treatment outcomes are not guaranteed.</small></p>
                </div>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script>
        // Mobile menu toggle
        const mobileToggle = document.querySelector('.mobile-menu-toggle');
        const nav = document.querySelector('.nav');
        
        mobileToggle.addEventListener('click', () => {
            nav.classList.toggle('active');
            mobileToggle.classList.toggle('active');
        });

        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Insurance form submission
        document.getElementById('insurance-form').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Thank you! An insurance specialist will call you within 10 minutes to verify your benefits.');
        });

        // Header scroll effect
        window.addEventListener('scroll', () => {
            const header = document.querySelector('.header');
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    </script>
</body>
</html>
```

## styles.css

```css
/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #333;
    overflow-x: hidden;
}

/* CSS Variables */
:root {
    --primary-navy: #1d2758;
    --primary-orange: #c77124;
    --light-navy: #2a3a6b;
    --light-orange: #d68332;
    --dark-navy: #161f47;
    --cream: #faf8f5;
    --white: #ffffff;
    --gray-100: #f8f9fa;
    --gray-200: #e9ecef;
    --gray-300: #dee2e6;
    --gray-400: #ced4da;
    --gray-500: #adb5bd;
    --gray-600: #6c757d;
    --gray-700: #495057;
    --gray-800: #343a40;
    --gray-900: #212529;
    --success: #28a745;
    --warning: #ffc107;
    --danger: #dc3545;
    --info: #17a2b8;
    
    --font-heading: 'Playfair Display', Georgia, serif;
    --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.15);
    --shadow-lg: 0 8px 24px rgba(0,0,0,0.2);
    --shadow-xl: 0 16px 48px rgba(0,0,0,0.25);
    
    --border-radius: 8px;
    --border-radius-lg: 16px;
    --border-radius-xl: 24px;
    
    --transition-fast: 0.2s ease;
    --transition-medium: 0.3s ease;
    --transition-slow: 0.5s ease;
}

/* Utility Classes */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.section-badge {
    display: inline-block;
    background: linear-gradient(135deg, var(--primary-orange), var(--light-orange));
    color: white;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 16px;
}

.section-title {
    font-family: var(--font-heading);
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 700;
    color: var(--primary-navy);
    margin-bottom: 20px;
    line-height: 1.2;
}

.section-subtitle {
    font-size: 18px;
    color: var(--gray-600);
    max-width: 600px;
    margin: 0 auto 40px;
    line-height: 1.6;
}

.section-header {
    text-align: center;
    margin-bottom: 60px;
}

/* Crisis Banner */
.crisis-banner {
    background: var(--danger);
    color: white;
    padding: 10px 0;
    text-align: center;
    position: relative;
    z-index: 1000;
    animation: pulse-bg 2s infinite;
}

@keyframes pulse-bg {
    0%, 100% { background: var(--danger); }
    50% { background: #c82333; }
}

.crisis-banner .container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
}

.crisis-pulse {
    width: 8px;
    height: 8px;
    background: white;
    border-radius: 50%;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.2); }
}

.crisis-text {
    font-weight: 600;
    font-size: 14px;
}

.crisis-call {
    color: white;
    text-decoration: none;
    font-weight: 700;
    font-size: 16px;
    padding: 5px 15px;
    border: 2px solid white;
    border-radius: 20px;
    transition: var(--transition-fast);
}

.crisis-call:hover {
    background: white;
    color: var(--danger);
}

/* Header */
.header {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 999;
    transition: var(--transition-medium);
    border-bottom: 1px solid var(--gray-200);
    margin-top: 44px;
}

.header.scrolled {
    background: rgba(255, 255, 255, 0.98);
    box-shadow: var(--shadow-md);
}

.header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 15px 0;
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo-img {
    width: 50px;
    height: 50px;
    object-fit: contain;
}

.logo-text h1 {
    font-family: var(--font-heading);
    font-size: 24px;
    font-weight: 700;
    color: var(--primary-navy);
    line-height: 1;
}

.tagline {
    font-size: 12px;
    color: var(--primary-orange);
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.nav {
    display: flex;
    align-items: center;
    gap: 30px;
}

.nav a {
    text-decoration: none;
    color: var(--gray-700);
    font-weight: 500;
    font-size: 15px;
    position: relative;
    transition: var(--transition-fast);
}

.nav a:hover {
    color: var(--primary-orange);
}

.nav a::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--primary-orange);
    transition: var(--transition-fast);
}

.nav a:hover::after {
    width: 100%;
}

.btn-header-call {
    background: var(--primary-orange);
    color: white;
    text-decoration: none;
    padding: 12px 20px;
    border-radius: var(--border-radius);
    font-weight: 600;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: var(--transition-fast);
}

.btn-header-call:hover {
    background: var(--light-orange);
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.mobile-menu-toggle {
    display: none;
    flex-direction: column;
    cursor: pointer;
    gap: 4px;
}

.mobile-menu-toggle span {
    width: 24px;
    height: 2px;
    background: var(--primary-navy);
    transition: var(--transition-fast);
}

/* Hero Section */
.hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    align-items: center;
    overflow: hidden;
    padding-top: 120px;
}

.hero-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url('../images/hero-sunset.jpg');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    z-index: -2;
}

.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, 
        rgba(29, 39, 88, 0.85) 0%, 
        rgba(29, 39, 88, 0.7) 50%, 
        rgba(199, 113, 36, 0.3) 100%);
    z-index: -1;
}

.hero-content {
    display: grid;
    grid-template-columns: 1fr 1.5fr;
    gap: 60px;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
}

/* Crisis Side */
.hero-crisis {
    background: rgba(220, 53, 69, 0.95);
    backdrop-filter: blur(10px);
    padding: 40px;
    border-radius: var(--border-radius-xl);
    border: 2px solid rgba(255, 255, 255, 0.2);
    color: white;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.hero-crisis::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
    animation: shine 3s infinite;
}

@keyframes shine {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

.crisis-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.2);
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
}

.pulse-dot {
    width: 8px;
    height: 8px;
    background: white;
    border-radius: 50%;
    animation: pulse 1.5s infinite;
}

.hero-crisis h2 {
    font-family: var(--font-heading);
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 15px;
    line-height: 1.2;
}

.crisis-subtitle {
    font-size: 16px;
    opacity: 0.9;
    margin-bottom: 25px;
    line-height: 1.5;
}

.btn-crisis {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: white;
    color: var(--danger);
    text-decoration: none;
    padding: 15px 25px;
    border-radius: var(--border-radius);
    font-weight: 700;
    font-size: 16px;
    margin-bottom: 25px;
    transition: var(--transition-fast);
    box-shadow: var(--shadow-lg);
}

.btn-crisis:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-xl);
}

.crisis-features {
    display: grid;
    gap: 12px;
}

.feature-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 14px;
    font-weight: 500;
}

.check {
    width: 20px;
    height: 20px;
    background: var(--success);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    font-weight: bold;
}

/* Hope Side */
.hero-hope {
    color: white;
    text-align: left;
}

.trust-badges {
    display: flex;
    gap: 15px;
    margin-bottom: 25px;
    flex-wrap: wrap;
}

.trust-badge {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    padding: 8px 15px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.trust-badge.accredited {
    background: rgba(199, 113, 36, 0.9);
}

.hero-hope h1 {
    font-family: var(--font-heading);
    font-size: clamp(2.5rem, 6vw, 4rem);
    font-weight: 900;
    margin-bottom: 25px;
    line-height: 1.1;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.hero-subtitle {
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 35px;
    opacity: 0.95;
}

.hero-stats {
    display: flex;
    gap: 30px;
    margin-bottom: 35px;
}

.stat-item {
    text-align: center;
}

.stat-number {
    font-family: var(--font-heading);
    font-size: 32px;
    font-weight: 900;
    color: var(--primary-orange);
    line-height: 1;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.stat-label {
    font-size: 14px;
    font-weight: 500;
    opacity: 0.9;
    margin-top: 5px;
}

.hero-actions {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
}

.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: var(--primary-orange);
    color: white;
    text-decoration: none;
    padding: 15px 25px;
    border-radius: var(--border-radius);
    font-weight: 700;
    font-size: 16px;
    transition: var(--transition-fast);
    box-shadow: var(--shadow-lg);
}

.btn-primary:hover {
    background: var(--light-orange);
    transform: translateY(-2px);
    box-shadow: var(--shadow-xl);
}

.btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    color: white;
    text-decoration: none;
    padding: 15px 25px;
    border-radius: var(--border-radius);
    font-weight: 600;
    font-size: 16px;
    border: 2px solid rgba(255, 255, 255, 0.3);
    transition: var(--transition-fast);
}

.btn-secondary:hover {
    background: rgba(255, 255, 255, 0.2);
    border-color: rgba(255, 255, 255, 0.5);
    transform: translateY(-2px);
}

.btn-arrow {