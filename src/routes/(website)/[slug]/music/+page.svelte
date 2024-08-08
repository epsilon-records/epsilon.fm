<script>
	import { Spotify } from 'sveltekit-embed';
	import { Badge } from '$lib/components/ui/badge';
	// import { createQuery } from '@tanstack/svelte-query';
	// import { ArtistsService } from '$lib/api/ms/client/services.gen';
	// import { error } from '@sveltejs/kit';

	// export let data;

	// const artist = createQuery({
	// 	queryKey: ['artists', data.org_id],
	// 	queryFn: async () => api().getArtist(data.org_id),
	// 	staleTime: 5 * 60 * 1000 // 5 minutes
	// });
	// $: if ($artist.error) {
	// 	error(404);
	// }
</script>

<svelte:head>
	<title>Vozz Rich — About</title>
</svelte:head>

<div class="container">
	<div class="content">
		<h1 class="text-white">Music</h1>
		<p class="bg-slate-900 p-4 text-white">
			Listen on <Badge class="m-2">Spotify</Badge> or purchase on <Badge class="m-2">Beatport</Badge
			>
		</p>
		<br />
		<Spotify height="600px" width="900px" spotifyLink="artist/27sSKrytmUXukDnMGPXNHQ" />
		<br />
	</div>
</div>

<style>
	.container {
		max-width: 900px;
		padding: 0;
		justify-content: center;
	}

	.content {
		max-width: 100%;
		min-height: 500px;
		text-align: left;
		margin: 0 auto;
		box-sizing: border-box;
	}

	h1 {
		font-weight: 700;
		margin: 0 0 50px 0;
		font-size: 36px;
		text-align: start;
	}
</style>
