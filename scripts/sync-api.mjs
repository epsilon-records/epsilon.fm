import { execSync } from 'child_process';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

// Get the directory name of the current module file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load environment variables from .env file
dotenv.config({ path: path.resolve(__dirname, '../backend/.env') });

const apiSyncCommand = `bunx rdme openapi ${process.env.README_OPENAPI_URL}/openapi.json --key=${process.env.README_API_KEY} --id=${process.env.README_SYNC_ID}`;
execSync(apiSyncCommand, { stdio: 'inherit' });
