<!-- Updated: 2025-09-21 14:39:03 UTC -->

<!-- CRITICAL: OMIT NOT APPLICABLE BULLET-POINTS AND SECTIONS -->

# {PROJECT_NAME} - System Architecture


## OVERVIEW

**Design Philosophy**: {DESIGN_PHILOSOPHY}
**Scalability Target**: {SCALABILITY_TARGET}


## SYSTEM DESIGN PRINCIPLES

1. **{PRINCIPLE_1}**: {PRINCIPLE_1_RATIONALE}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->


## HIGH-LEVEL ARCHITECTURE

### System Components

```
{ARCHITECTURE_DIAGRAM}
```

### Core Modules

- **{MODULE_1}**: {MODULE_1_DESCRIPTION}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### Layer Architecture

1. **Presentation Layer**
   - {PRESENTATION_TECH}
   - {PRESENTATION_RESPONSIBILITIES}
   - {PRESENTATION_PATTERNS}

2. **Application Layer**
   - {APPLICATION_LOGIC}
   - {APPLICATION_PATTERNS}
   - {APPLICATION_TRANSACTIONS}

3. **Domain Layer**
   - {DOMAIN_MODELS}
   - {DOMAIN_RULES}
   - {DOMAIN_SERVICES}

4. **Infrastructure Layer**
   - {INFRASTRUCTURE_PERSISTENCE}
   - {INFRASTRUCTURE_INTEGRATIONS}
   - {INFRASTRUCTURE_CONCERNS}


## DATA ARCHITECTURE

### Data Models

**Primary Entities**:
- **{ENTITY_1}**: {ENTITY_1_DESCRIPTION}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### Data Flow

1. **{FLOW_1}**: {FLOW_1_SOURCE} → {FLOW_1_PROCESSING} → {FLOW_1_DESTINATION}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### Storage Strategy

- **Primary Database**: {PRIMARY_DATABASE}
- **Cache Layer**: {CACHE_STRATEGY}
- **File Storage**: {FILE_STORAGE}
- **Data Retention**: {DATA_RETENTION}


## API ARCHITECTURE

### API Design Standards

- **Protocol**: [REST | GraphQL | gRPC | WebSocket]
- **Authentication**: {AUTHENTICATION_METHOD}
- **Authorization**: {AUTHORIZATION_APPROACH}
- **Versioning**: {API_VERSIONING_STRATEGY}

### Core APIs

1. **{API_GROUP_1}**
   - Endpoint Pattern: `/api/v1/{RESOURCE_1}`
   - Purpose: {API_GROUP_1_PURPOSE}
   - Key Operations: {API_GROUP_1_OPERATIONS}

<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### Integration Points

- **{EXTERNAL_SERVICE_1}**: {EXTERNAL_SERVICE_1_INTEGRATION}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->


## SECURITY ARCHITECTURE

### Security Layers

1. **Network Security**
   - {FIREWALL_POLICIES}
   - {DDOS_PROTECTION}
   - {SSL_TLS_CONFIG}

2. **Application Security**
   - {AUTH_MECHANISM}
   - {AUTHZ_FRAMEWORK}
   - {SESSION_MANAGEMENT}

3. **Data Security**
   - {ENCRYPTION_AT_REST}
   - {ENCRYPTION_IN_TRANSIT}
   - {KEY_MANAGEMENT}

<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### Security Standards

- **Compliance**: {REGULATORY_REQUIREMENTS}
- **Audit**: {AUDIT_APPROACH}
- **Incident Response**: {INCIDENT_HANDLING}


## INFRASTRUCTURE ARCHITECTURE

### Deployment Architecture

- **Environment Strategy**: {ENVIRONMENT_STRATEGY}
- **Containerization**: {CONTAINER_STRATEGY}
- **CI/CD Pipeline**: {CICD_AUTOMATION}
- **Infrastructure as Code**: {IAC_APPROACH}

### Scalability Design

1. **Horizontal Scaling**
   - {LOAD_BALANCING_STRATEGY}
   - {AUTO_SCALING_POLICIES}
   - {SERVICE_DISCOVERY}

2. **Vertical Scaling**
   - {RESOURCE_OPTIMIZATION}
   - {PERFORMANCE_TUNING}

### High Availability

- **Redundancy**: {REDUNDANCY_APPROACH}
- **Failover**: {FAILOVER_MECHANISMS}
- **Disaster Recovery**: {BACKUP_RECOVERY_STRATEGY}
- **SLA Target**: {UPTIME_REQUIREMENTS}


## PERFORMANCE ARCHITECTURE

### Performance Requirements

- **Response Time**: {TARGET_LATENCY}
- **Throughput**: {REQUESTS_PER_SECOND}
- **Concurrent Users**: {EXPECTED_LOAD}
- **Data Volume**: {DATA_PROCESSING_CAPACITY}

### Optimization Strategies

1. **Caching Strategy**
   - {CACHE_LEVELS_INVALIDATION}
   - {CDN_UTILIZATION}

2. **Database Optimization**
   - {QUERY_OPTIMIZATION}
   - {INDEXING_STRATEGY}
   - {CONNECTION_POOLING}

3. **Async Processing**
   - {MESSAGE_QUEUING}
   - {BACKGROUND_JOBS}
   - {EVENT_STREAMING}


## MONITORING & OBSERVABILITY

### Monitoring Stack

- **Metrics**: {METRICS_COLLECTION_VISUALIZATION}
- **Logging**: {CENTRALIZED_LOGGING_APPROACH}
- **Tracing**: {DISTRIBUTED_TRACING_IMPLEMENTATION}
- **Alerting**: {ALERT_RULES_ESCALATION}

### Key Metrics

- **System Health**: {HEALTH_CHECK_ENDPOINTS}
- **Business Metrics**: {KPI_TRACKING}
- **Performance Metrics**: {RESPONSE_TIMES_ERROR_RATES}
- **Resource Utilization**: {CPU_MEMORY_DISK_NETWORK}


## TECHNOLOGY DECISIONS

### Architecture Decision Records (ADRs)

1. **ADR-001**: {ADR_001_DECISION}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->

### Trade-offs

- **{TRADEOFF_1}**: {TRADEOFF_1_IMPLICATIONS}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->


## MIGRATION & EVOLUTION

### Migration Strategy

- **Current State**: {CURRENT_STATE}
- **Target State**: {TARGET_STATE}
- **Migration Path**: {MIGRATION_PATH}
- **Rollback Plan**: {ROLLBACK_PLAN}

### Future Considerations

1. **{ENHANCEMENT_1}**: {ENHANCEMENT_1_DESCRIPTION}
<!-- CRITICAL: REPEAT PATTERN FOR EACH ITEM -->
