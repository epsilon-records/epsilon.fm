import { SvelteKitAuth } from '@auth/sveltekit';
import Google from '@auth/sveltekit/providers/google';
import GitHub from '@auth/sveltekit/providers/github';
import Spotify from '@auth/sveltekit/providers/spotify';
import { DrizzleAdapter } from '@auth/drizzle-adapter';
import { db } from './schema';

export const { handle, signIn, signOut } = SvelteKitAuth({
	adapter: DrizzleAdapter(db),
	providers: [Google]
});
