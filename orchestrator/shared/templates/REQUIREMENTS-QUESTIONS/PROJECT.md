<!-- Updated: 2025-10-10 18:36:41 UTC -->

# Project Scope Questions Template

Structured question set for enriching project-level planning context.


## QUESTION SET OVERVIEW

**Total Questions**: 6-7 questions
**Estimated Time**: 5-7 minutes
**User Option**: Can skip any or all questions for informed assumptions


## TECHNICAL REQUIREMENTS QUESTIONS

### Question 1: Platform & Deployment
**Ask**: "What platforms must this support (web, mobile, desktop), and where will it be deployed (cloud, on-premise, specific provider)?"

**Listening For**:
- Target platforms (browser, iOS, Android, desktop, etc.)
- Deployment environment (AWS, Azure, GCP, on-prem, hybrid)
- Infrastructure constraints
- Accessibility requirements

**Follow-up if unclear**: "Do you have existing infrastructure or hosting preferences?"


### Question 2: Technology Preferences
**Ask**: "Do you have technology preferences or constraints (programming languages, frameworks, databases)?"

**Listening For**:
- Language preferences (Python, JavaScript/TypeScript, Java, Go, etc.)
- Framework familiarity or requirements
- Database preferences (PostgreSQL, MySQL, MongoDB, etc.)
- Existing technology stack to integrate with

**Follow-up if unclear**: "What technologies is your team most comfortable with?"


### Question 3: Integration Requirements
**Ask**: "What existing systems, services, or APIs must this integrate with?"

**Listening For**:
- Third-party service dependencies (Stripe, Auth0, AWS services, etc.)
- Internal system integrations
- Data sources or sinks
- Authentication providers

**Follow-up if unclear**: "Will this be standalone or need to connect to existing systems?"


### Question 4: Performance & Scale
**Ask**: "What are your performance expectations (response times, concurrent users) and scalability needs?"

**Listening For**:
- Response time requirements (sub-second, real-time, etc.)
- Concurrent user targets
- Data volume expectations
- Growth projections

**Follow-up if unclear**: "Is this expected to handle 10s, 100s, 1000s, or more concurrent users?"


### Question 5: Security & Compliance
**Ask**: "What security or compliance requirements apply (GDPR, HIPAA, SOC2, etc.)?"

**Listening For**:
- Regulatory compliance needs
- Data privacy requirements
- Security certifications needed
- Industry-specific requirements

**Follow-up if unclear**: "Will you handle sensitive data like PII, payment info, or health records?"


### Question 6: Team Technical Context
**Ask**: "What's your team's technical expertise and familiarity with different technologies?"

**Listening For**:
- Programming language proficiency
- Framework experience
- Infrastructure management skills
- Testing practices

**Follow-up if unclear**: "What technologies does your team have the most experience with?"


### Question 7: Development Environment (Optional)
**Ask**: "What development tools and environments does your team use?"

**Listening For**:
- IDEs and editors
- Version control practices
- CI/CD tools
- Testing frameworks
- Containerization (Docker, etc.)

**Follow-up if unclear**: "Are there specific tools or workflows your team prefers?"


## VALIDATION CHECKLIST

After collecting answers, validate understanding:

```
Let me confirm my understanding:

**Technical Requirements**:
- Platform: [restate]
- Technology: [restate]
- Integrations: [restate]
- Performance: [restate]
- Security: [restate]

**Team Context**:
- Expertise: [restate]
- Tools: [restate if answered]

Did I capture this correctly? Any corrections or additions?
```


## SKIP ASSUMPTIONS

If user skips questions, document these assumptions:

**Technical Assumptions**:
- Modern web stack (React/Next.js or Vue/Nuxt)
- Cloud deployment (Vercel, AWS, or similar)
- PostgreSQL or similar relational database
- Standard REST or GraphQL APIs
- OAuth2/JWT authentication
- Responsive web design for mobile and desktop

**Security Assumptions**:
- Standard security best practices
- HTTPS/TLS encryption
- Password hashing (bcrypt/Argon2)
- CSRF/XSS protection
- Regular security updates

**Team Assumptions**:
- Modern JavaScript/TypeScript expertise
- Git version control
- Standard testing practices

**Architecture Assumptions**:
- Monolithic or modular monolith initially
- Microservices only if clearly needed
- Separation of concerns (frontend/backend/database)
- Test-driven development approach
- CI/CD pipeline for automated deployment
