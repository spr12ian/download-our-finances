# Customize these
GOOGLE_SERVICE_ACCOUNT_KEY ?= service-account.json
GOOGLE_PROJECT_ID ?= your-project-id

# Configuration
VENV_DIR := .venv
PYTHON := python3
REQUIREMENTS := requirements.txt
TOP_LEVEL_PACKAGES := google-auth gspread mypy pyyaml types-PyYAML

.PHONY: all setup activate clean freeze install-gcloud auth set-project info gcloud

all: setup test

setup:
	@echo "🔧 Creating virtual environment in $(VENV_DIR) if it doesn't exist..."
	@test -d $(VENV_DIR) || $(PYTHON) -m venv $(VENV_DIR)
	@echo "🚀 Upgrading pip, setuptools, and wheel..."
	. $(VENV_DIR)/bin/activate && \
	pip install --upgrade pip setuptools wheel
ifeq ("$(wildcard $(REQUIREMENTS))","")
	@echo "📦 Installing top-level packages: $(TOP_LEVEL_PACKAGES)"
	. $(VENV_DIR)/bin/activate && \
	pip install $(TOP_LEVEL_PACKAGES)
	@echo "📝 Writing top-level-only requirements.txt"
	@echo "# Top-level dev dependencies" > $(REQUIREMENTS)
	@for pkg in $(TOP_LEVEL_PACKAGES); do echo $$pkg >> $(REQUIREMENTS); done
else
	@echo "📜 Installing from existing $(REQUIREMENTS)..."
	. $(VENV_DIR)/bin/activate && \
	pip install -r $(REQUIREMENTS)
endif
	@echo "✅ Setup complete."
	@echo "Run 'source $(VENV_DIR)/bin/activate' to activate the virtual environment."


activate:
	@echo "Run this to activate the virtual environment:"
	@echo "source $(VENV_DIR)/bin/activate"

freeze:
	@echo "📌 Rewriting $(REQUIREMENTS) with top-level-only packages..."
	@echo "# Top-level dev dependencies" > $(REQUIREMENTS)
	@for pkg in $(TOP_LEVEL_PACKAGES); do echo $$pkg >> $(REQUIREMENTS); done
	@echo "✅ Updated."

clean:
	@echo "🧹 Removing virtual environment..."
	@rm -rf $(VENV_DIR)
	@echo "🧹 Removing all __pycache__ directories..."
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@echo "🧹 Removing .mypy_cache directory..."
	@rm -rf .mypy_cache
	@echo "🧹 Removing log files..."
	@rm -rf *.log
	@echo "🧹 Removing requirements.txt ..."
	@rm -rf requirements.txt
	@echo "✅ Cleaned all caches and virtual environment."

test:
	@echo "Running tests..."
	@. $(VENV_DIR)/bin/activate && \
	pwl key_check
#	@. $(VENV_DIR)/bin/activate && \
	pytest --maxfail=1 --disable-warnings -q
	@echo "✅ Tests completed."

gcloud: install-gcloud auth set-project info

# Install the Google Cloud SDK
install-gcloud:
	@echo "Installing Google Cloud SDK..."
	sudo apt-get update -y && \
	sudo apt-get install -y apt-transport-https ca-certificates gnupg curl && \
	echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \
		| sudo tee /etc/apt/sources.list.d/google-cloud-sdk.list && \
	curl https://packages.cloud.google.com/apt/doc/apt-key.gpg \
		| sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && \
	sudo apt-get update -y && \
	sudo apt-get install -y google-cloud-sdk

auth:
	@echo "🔐 Authenticating with service account..."
	@if echo '$(GOOGLE_SERVICE_ACCOUNT_KEY)' | grep -q '^{'; then \
		echo "📝 Writing inline JSON to .gsa-tmp.json"; \
		echo '$(GOOGLE_SERVICE_ACCOUNT_KEY)' > .gsa-tmp.json; \
		gcloud auth activate-service-account --key-file=.gsa-tmp.json; \
		rm .gsa-tmp.json; \
	else \
		if [ ! -f "$(GOOGLE_SERVICE_ACCOUNT_KEY)" ]; then \
			echo "❌ File not found: $(GOOGLE_SERVICE_ACCOUNT_KEY)"; \
			exit 1; \
		fi; \
		echo "📁 Using service account file: $(GOOGLE_SERVICE_ACCOUNT_KEY)"; \
		gcloud auth activate-service-account --key-file="$(GOOGLE_SERVICE_ACCOUNT_KEY)"; \
	fi



# Set active project
set-project:
	@echo "Setting project to: $(GOOGLE_PROJECT_ID)"
	gcloud config set project $(GOOGLE_PROJECT_ID)

# Show current configuration
info:
	@echo "GOOGLE_PROJECT_ID=$(GOOGLE_PROJECT_ID)"
	@echo "GOOGLE_SERVICE_ACCOUNT_KEY:"
	@if echo '$(GOOGLE_SERVICE_ACCOUNT_KEY)' | grep -q '^{'; then \
		echo '$(GOOGLE_SERVICE_ACCOUNT_KEY)' | jq .; \
	else \
		cat "$(GOOGLE_SERVICE_ACCOUNT_KEY)" | jq .; \
	fi
#	@gcloud config list

