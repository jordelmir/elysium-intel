BEGIN;
DROP TABLE IF EXISTS hardware_parsed CASCADE;
DROP TABLE IF EXISTS hardware_raw CASCADE;

CREATE TABLE hardware_raw (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sha256 BYTEA NOT NULL,
    source_device TEXT NOT NULL,
    raw_dump BYTEA NOT NULL CHECK (octet_length(raw_dump) <= 4096),
    hmac_signature BYTEA NOT NULL CHECK (octet_length(hmac_signature) = 32),
    nonce TEXT NOT NULL,
    ingested_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE (source_device, nonce)
);

CREATE TABLE hardware_parsed (
    raw_id UUID PRIMARY KEY REFERENCES hardware_raw(id),
    parser_version TEXT NOT NULL,
    structural_hash BYTEA NOT NULL CHECK (octet_length(structural_hash) = 32),
    health NUMERIC(4,1),
    cycles INT,
    confidence FLOAT CHECK (confidence BETWEEN 0 AND 1),
    anomaly_score FLOAT DEFAULT 0.0,
    anomaly_type TEXT,
    parsed_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_parsed_hash ON hardware_parsed(structural_hash);
CREATE INDEX idx_raw_ingested ON hardware_raw(ingested_at DESC);

-- WORM Protection
REVOKE UPDATE, DELETE ON hardware_raw FROM PUBLIC;
COMMIT;
