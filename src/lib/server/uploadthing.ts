import { createUploadthing } from 'uploadthing/server';
import type { FileRouter } from 'uploadthing/server';
import logger from '$lib/logger';

const f = createUploadthing();

const auth = (req: Request) => ({ id: 'fakeId', req: req }); // Fake auth function

// FileRouter for your app, can contain multiple FileRoutes
export const ourFileRouter = {
	// Define as many FileRoutes as you like, each with a unique routeSlug
	imageUploader: f({ image: { maxFileSize: '4MB' } })
		// Set permissions and file types for this FileRoute
		.middleware(async ({ req }) => {
			// This code runs on your server before upload
			const user = await auth(req);

			// If you throw, the user will not be able to upload
			if (!user) throw new Error('Unauthorized');

			// Whatever is returned here is accessible in onUploadComplete as `metadata`
			return { userId: user.id };
		})
		.onUploadComplete(async ({ metadata, file }) => {
			// This code RUNS ON YOUR SERVER after upload
			logger.info('Upload complete for userId:', metadata.userId);
			logger.info('file url', file.url);
		})
} satisfies FileRouter;

export type OurFileRouter = typeof ourFileRouter;
