# Hospital Secure Threat Model
# Secure Architecture & Design: Healthcare Appointment System
**Student:** Taha Hunaid Ali 
**Course:** Secure Architecture and Design  
**Due Date:** February 28, 2026  

## Executive Summary
This project presents a secure-by-design architecture for a Healthcare Appointment System. Given the sensitivity of Protected Health Information (PHI), the design focuses on strong identity management, network segmentation, and data encryption to meet HIPAA-level security standards.

## Task 1: System Definition & Architecture

### Application Components
- Patient Portal: Web/Mobile frontend for booking and viewing records.
- Doctor Portal: Management interface for schedules and consultation notes.
- API Gateway: Central entry point for routing, rate limiting, and initial authentication.
- Microservices: Identity Service (Auth), Appointment Service, and Patient Record Service.
- Data Stores: User Database (Credentials) and Health Record DB (Encrypted Clinical Data).

### High-Level Architecture Diagram
```mermaid
graph TD
    subgraph Public_Internet [External Zone]
        P[Patient App]
        D[Doctor Portal]
    end

    subgraph DMZ [Inspection Zone]
        WAF[WAF / API Gateway]
    end

    subgraph Private_App_Net [Internal Trust Boundary]
        Auth[Identity Service]
        Appt[Appointment Service]
        PHI_Svc[Health Record Service]
    end

    subgraph Data_Layer [Secure Storage Zone]
        UDB[(User DB)]
        HDB[(Encrypted Health DB)]
        Vault[Secrets Manager]
    end

    P --> WAF
    D --> WAF
    WAF --> Auth
    WAF --> Appt
    WAF --> PHI_Svc
    Auth --> UDB
    PHI_Svc --> HDB
    Auth -.-> Vault
    PHI_Svc -.-> Vault
