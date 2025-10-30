## ADDED Requirements
### Requirement: Load Aggregated Data Format
The system SHALL load CSV files with aggregated A/B test data in the format: `group,success,total` where each row represents a variant.

#### Scenario: Load aggregated CSV
- **WHEN** a CSV file contains columns `group`, `success`, and `total` with rows for variants A and B
- **THEN** the system SHALL parse the file and extract success counts and total counts for each variant

#### Scenario: Handle missing or invalid data
- **WHEN** the CSV file has missing values, invalid formats, or unexpected group names
- **THEN** the system SHALL raise appropriate errors with clear messages

### Requirement: Load Row-Level Data Format
The system SHALL load CSV files with row-level A/B test data in the format: `user_id,group,converted` and aggregate to counts.

#### Scenario: Load and aggregate row-level CSV
- **WHEN** a CSV file contains columns `user_id`, `group`, and `converted` (0/1) with multiple rows per variant
- **THEN** the system SHALL aggregate the data to compute success counts and total counts for each variant

#### Scenario: Compute aggregated counts from row-level data
- **WHEN** row-level data is loaded
- **THEN** the system SHALL compute total counts per group and success counts (sum of converted=1) per group

