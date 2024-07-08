import { UPLOADTHING_SECRET } from '$env/static/private';
import { ourFileRouter } from '$lib/server/uploadthing';

import { createRouteHandler } from 'uploadthing/server';

// The Svelte extension complains if you export the handlers directly
const { GET, POST } = createRouteHandler({
	router: ourFileRouter,
	config: {
		uploadthingSecret: UPLOADTHING_SECRET
	}
});

export { GET, POST };
