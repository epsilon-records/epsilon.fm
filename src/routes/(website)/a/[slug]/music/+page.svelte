<script>
	import { Spotify } from 'sveltekit-embed';
	import skills from '../Skills';
	export let data;
</script>

<svelte:head>
	<title>{data.stageName} — About</title>
</svelte:head>

<div class="container">
	<h1 class="text-white">Music</h1>
	<br />
	<Spotify height="600px" width="740px" spotifyLink="artist/27sSKrytmUXukDnMGPXNHQ" />
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
