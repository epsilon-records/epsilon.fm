import { execSync } from 'child_process';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

// Get the directory name of the current module file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load environment variables from .env file
dotenv.config({ path: path.resolve(__dirname, '../backend/.env') });

const apiSyncCommand = `bunx rdme openapi https://api.epsilon.fm/openapi.json --key=${process.env.README_API_KEY} --id=66994c8f15ee25004370d87d`;
execSync(apiSyncCommand, { stdio: 'inherit' });
