<script lang="ts">
	import Burger from './Hamburger.svelte';
	import logo from '$lib/images/logo.png';
	import routes from './NavRoutes';
	import { modalOpened } from '$lib/stores/website';
	let opened = false;
	export let segment: string;
	export let data;
</script>

<div class={opened ? 'NavBar open' : 'NavBar'}>
	<div class="innerContainer">
		<a href="https://epsilon.fm">
			<img src={logo} alt="logo" class="logo" />
		</a>
		<div class="burger">
			<Burger bind:open={opened} />
		</div>
		<div class="buttons">
			{#each routes as route}
				{#if route.href === '/merch'}
					<a class={`button`} href="https://epsilonrecords.nl{route.href}/{data.slug}"
						>{route.label}</a
					>
				{:else if route.href === '/contact'}
					<div
						class="button"
						role="button"
						tabindex="0"
						on:keypress={() => {
							modalOpened.set(true);
						}}
						on:click={() => {
							modalOpened.set(true);
						}}
					>
						{route.label}
					</div>
				{:else}
					<a
						class={`button ${segment === '/a/' + data.slug + route.href ? 'selected' : ''}`}
						href="/a/{data.slug}{route.href}">{route.label}</a
					>
				{/if}
			{/each}
		</div>
	</div>
	<div class="responsiveButtons buttons">
		{#each routes as route}
			{#if route.href === '/merch'}
				<a class={`button`} href="https://epsilonrecords.nl{route.href}/{data.slug}"
					>{route.label}</a
				>
			{:else if route.href === '/contact'}
				<a class={`button`} href="https://epsilonrecords.nl{route.href}">{route.label}</a>
			{:else}
				<a
					class={`button ${segment === '/a/' + data.slug + route.href ? 'selected' : ''}`}
					href="/a/{data.slug}{route.href}">{route.label}</a
				>
			{/if}
		{/each}
	</div>
</div>

<style>
	:global(.logo) {
		cursor: pointer;
		height: 30px;
		width: 30px;
	}

	.open {
		flex-direction: column !important;
		align-items: center !important;
		height: 330px !important;
		transition: height 0.2s cubic-bezier(0.455, 0.03, 0.515, 0.955);
	}

	.selected {
		position: relative;
		color: white;
	}

	.button:hover::after {
		content: '';
		background: #ca3c25;
		display: block;
		height: 3px;
		width: 100%;
		position: absolute;
		bottom: 0;
	}

	.button.selected:after {
		content: '';
		background: #ca3c25;
		display: block;
		height: 3px;
		width: 100%;
		position: absolute;
		bottom: 0;
	}

	.innerContainer {
		display: flex;
		justify-content: space-between;
		align-items: center;
		width: 100%;
		max-width: 900px;
		box-sizing: border-box;
	}

	.innerContainer :global(a) {
		height: 30px;
		color: white;
	}

	.NavBar {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		align-items: center;
		width: 100%;
		max-width: 900px;
		box-sizing: border-box;
		padding: 20px;
		height: 80px;
		overflow: hidden;
		transition: height 0.2s cubic-bezier(0.455, 0.03, 0.515, 0.955);
	}

	.buttons {
		display: none;
		justify-content: space-between;
		align-items: center;
		font-weight: 500;
	}

	.responsiveButtons {
		margin-top: 20px;
		width: 100%;
		display: flex !important;
		flex-direction: column;
	}

	.responsiveButtons .button {
		max-width: 100px;
		width: 100%;
		text-align: center;
	}

	.buttons .button {
		padding: 0;
		cursor: pointer;
		transition: color 0.2s ease-in-out;
		text-decoration: none;
		position: relative;
		margin: 10px;
		color: white;
	}

	.button.selected {
		color: white;
	}

	.burger :global(button) {
		margin: 0;
	}

	@media (min-width: 900px) {
		.NavBar {
			padding: 20px 0;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
			max-width: 900px;
			margin: 0 auto;
		}

		.buttons {
			display: flex;
		}

		.NavBar .burger {
			display: none !important;
		}
		.responsiveButtons {
			display: none !important;
		}
	}
</style>
