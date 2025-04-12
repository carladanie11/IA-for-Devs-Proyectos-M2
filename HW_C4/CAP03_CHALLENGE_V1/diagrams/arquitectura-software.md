graph TD
    subgraph Frontend
        A[Web App]
        B[Mobile App]
    end

    subgraph Backend
        C[Load Balancer]
        D[Booking Service]
        E[Authentication Service]
        F[Inventory Service]
        G[Payment Service]
        H[Notification Service]
        I[External API Integrator]
    end

    subgraph DatabaseLayer
        J[User Database]
        K[Booking Database]
        L[Inventory Database]
        M[Payment Database]
    end

    subgraph ThirdPartyServices
        N[Payment Gateway (Stripe/PayPal)]
        O[External Booking Platforms (Booking.com, Expedia)]
        P[Email/SMS Service]
    end

    A --> C
    B --> C
    C --> D
    C --> E
    C --> F
    D --> K
    E --> J
    F --> L
    G --> M
    G --> N
    H --> P
    I --> O
    D --> G
    D --> H
    D --> I