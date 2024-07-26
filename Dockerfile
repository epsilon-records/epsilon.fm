FROM oven/bun
WORKDIR /app

# Install Node.js 20, make, and other build essentials
RUN apt-get update && apt-get install -y curl make build-essential && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy package.json and bun.lockb first
COPY package.json ./

# Install dependencies
RUN bun install

# Copy the rest of the application files
COPY . .

# Build application
RUN bun run build

# Set environment
ENV NODE_ENV=development