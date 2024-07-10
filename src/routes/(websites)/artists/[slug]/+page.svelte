<script>
	import FaLinkedin from 'svelte-icons/fa/FaLinkedin.svelte';
	import FaSoundcloud from 'svelte-icons/fa/FaSoundcloud.svelte';
	import FaFacebook from 'svelte-icons/fa/FaFacebook.svelte';
	import FaInstagram from 'svelte-icons/fa/FaInstagram.svelte';
	import FaEnvelope from 'svelte-icons/fa/FaEnvelope.svelte';
	import FaMedium from 'svelte-icons/fa/FaMedium.svelte';
	import { modalOpened } from '$lib/stores/website';

	/** @type {import('./$types').PageData} */
	export let data;
</script>

<svelte:head>
	<title>{data.stageName}</title>
</svelte:head>
<main>
	<h1>{data.stageName}</h1>
	<h3>{data.currentLocation}</h3>
	<div class="icons">
		<div
			role="button"
			tabindex="0"
			on:keypress={() => {
				modalOpened.set(true);
			}}
			on:click={() => {
				modalOpened.set(true);
			}}
		>
			<div class="icon">
				<FaEnvelope />
			</div>
		</div>

		{#if data.instagramProfileLink}
			<a
				href={data.instagramProfileLink}
				aria-label="Instagram"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<FaInstagram />
				</div>
			</a>
		{/if}
		{#if data.facebookProfileLink}
			<a
				href={data.facebookProfileLink}
				aria-label="Facebook"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<FaFacebook />
				</div>
			</a>
		{/if}
		{#if data.soundcloudProfileLink}
			<a
				href={data.soundcloudProfileLink}
				aria-label="SoundCloud"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<FaSoundcloud />
				</div>
			</a>
		{/if}
	</div>
</main>

<style>
	a {
		color: white;
		text-decoration: none;
	}
	main {
		text-align: center;
		padding: 0;
		margin: 0 auto;
		text-align: center;

		display: flex;
		flex-direction: column;
		height: calc(100vh - 80px - 88px);
		justify-content: center;
		align-items: center;
	}

	h1 {
		font-weight: 700;
	}

	main > h1 {
		margin: 50px 10px 0;
		font-size: 36px;
	}

	.icons {
		display: flex !important;
		justify-content: center !important;
		align-items: center;
		gap: 20px;
		cursor: pointer;
		font-size: 30px;
		display: flex;
		justify-content: space-between;
		max-width: 200px;
		margin: 50px auto 0;
	}

	.icon {
		cursor: pointer;
		transition: color 0.2s ease-in-out;
		width: 40px;
	}
	.icon:hover {
		color: #ca3c25;
	}

	@media (min-width: 900px) {
		main > h1 {
			font-size: 48px;
		}
	}

	@media (min-width: 600px) {
		main {
			max-width: none;
		}
	}
</style>
