# Security Policy for Patient Record Service
# Ensures the service can only read its own credentials and encrypt/decrypt data

path "secret/data/healthcare/db-creds" {
  capabilities = ["read"]
}

path "transit/encrypt/patient-phi" {
  capabilities = ["update"]
}

path "transit/decrypt/patient-phi" {
  capabilities = ["update"]
}

# Deny access to other sensitive paths by default
path "secret/data/admin/*" {
  capabilities = ["deny"]
}
