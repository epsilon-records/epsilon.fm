<script>
	import skills from '$lib/Skills';
	import { page } from '$app/stores';
	import { Spotify } from 'sveltekit-embed';
	/** @type {import('./$types').PageData} */
	export let data;

	$: stageName = data.stageName;
	$: biography = data.biography;
</script>

<svelte:head>
	<title>{stageName} — About</title>
</svelte:head>

<div class="container">
	<main>
		<h1>Music</h1>
		<Spotify spotifyLink="artist/27sSKrytmUXukDnMGPXNHQ" />
	</main>
</div>

<style>
	.container {
		max-width: 900px;
		padding: 0;
		display: flex;
		justify-content: center;
	}

	main {
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

	h2 {
		margin-top: 50px;
	}

	.list {
		display: flex;
		flex-direction: column;
		gap: 30px;
	}

	@media (min-width: 900px) {
		.list {
			flex-direction: row;
		}
		main > h1 {
			font-size: 48px;
		}
	}
</style>
