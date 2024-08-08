<script>
	import skills from '../Skills';
	import { Badge } from '$lib/components/ui/badge';
	// import { createQuery } from '@tanstack/svelte-query';
	// import { ArtistsService } from '$lib/api/ms/client/services.gen';
	// import { error } from '@sveltejs/kit';

	// export let data;

	// const artist = createQuery({
	// 	queryKey: ['artists', data.org_id],
	// 	queryFn: async () => ArtistsService.endpointV1ArtistsGetIdGet({ path: { id: data.org_id } })
	// });

	// $: if (artist.error) {
	// 	error(404);
	// }
</script>

<svelte:head>
	<title>Vozz Rich — About</title>
</svelte:head>

<div class="container">
	<div class="content">
		<h1 class="text-white">About</h1>
		<p class="bg-slate-900 p-4 text-white">
			Vozz Rich is a West Coast based EDM Producer, and winner of the 2023 Dallas EDM Awards for
			'Best House Track'. Vozz started his music career over 12 years ago with a focus on sound
			mastering and vinyl record DJ sets. He has produced, mixed, and engineered music for top DJ's
			and Artists. Labels signed with include Soave, Epsilon, Batuque, Maniana, & Lone Star Records.
			Vozz is an also an accomplished DJ, as he gets audiences moving with unique mixes and sounds
			that span Tech House and Latin EDM. Vozz's tracks and performance style never go unnoticed on
			a dance floor, as he brings high-energy and engagement to every performance.
		</p>
		<br />
		{#each Object.entries(skills) as [section, technologies]}
			<div class="w-min bg-slate-900 p-2 text-xs text-white">
				{section}:
			</div>

			{#each technologies as technology}
				<Badge class="m-2">{technology}</Badge>
			{/each}
		{/each}
	</div>
</div>

<style>
	.container {
		max-width: 900px;
		padding: 0;
		display: flex;
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
