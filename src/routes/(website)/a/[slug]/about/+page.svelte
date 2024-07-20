<script>
	import skills from '../Skills';
	import { Badge } from '$lib/components/ui/badge';
	import { createQuery } from '@tanstack/svelte-query';
	import { api } from '$lib/api/v1';
	import { error } from '@sveltejs/kit';
	export let data;

	const artist = createQuery({
		queryKey: ['artists'],
		queryFn: async () => api().getArtist(data.orgId)
	});
	if (!artist) {
		error(404);
	}
</script>

<svelte:head>
	<title>{$artist.data?.stageName} — About</title>
</svelte:head>

<div class="container">
	<div class="content">
		<h1 class="text-white">About</h1>
		<p class="bg-slate-900 p-4 text-white">{$artist.data?.biography}</p>
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
