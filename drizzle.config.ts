import { defineConfig } from 'drizzle-kit';

export default defineConfig({
	dialect: 'postgresql', // "mysql" | "sqlite" | "postgresql"
	schema: './src/lib/db/schema.ts',
	out: './drizzle'
});
