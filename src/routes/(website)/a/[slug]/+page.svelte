<script>
	import FaEnvelope from 'svelte-icons/fa/FaEnvelope.svelte';
	import SocialIcons from '@rodneylab/svelte-social-icons';
	import RiTiktokFill from 'svelte-remixicon/RiTiktokFill.svelte';
	import { modalOpened } from '$lib/stores/website';

	export let data;
</script>

<svelte:head>
	<title>{data.stageName}</title>
</svelte:head>
<main>
	<h1>{data.stageName.toUpperCase()}</h1>
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
				<SocialIcons network="email" fgColor="#FFFFFF" bgColor="transparent" />
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
					<SocialIcons network="instagram" fgColor="#FFFFFF" bgColor="transparent" />
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
					<SocialIcons network="facebook" fgColor="#FFFFFF" bgColor="transparent" />
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
					<SocialIcons network="soundcloud" fgColor="#FFFFFF" bgColor="transparent" />
				</div>
			</a>
		{/if}
		{#if data.bandsintownProfileLink}
			<a
				href={data.bandsintownProfileLink}
				aria-label="Bandsintown"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<SocialIcons network="bandsintown" fgColor="#FFFFFF" bgColor="transparent" />
				</div>
			</a>
		{/if}
		{#if data.tiktokProfileLink}
			<a
				href={data.tiktokProfileLink}
				aria-label="TikTok"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon pb-4 pl-2">
					<RiTiktokFill />
				</div>
			</a>
		{/if}
		{#if data.youtubeChannelLink}
			<a
				href={data.youtubeChannelLink}
				aria-label="YouTube"
				target="_blank"
				rel="noopener noreferrer"
			>
				<div class="icon">
					<SocialIcons network="youtube" fgColor="#FFFFFF" bgColor="transparent" />
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
