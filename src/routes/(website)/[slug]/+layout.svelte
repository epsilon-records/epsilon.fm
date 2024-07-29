<script lang="ts">
	import '$src/app.css';
	import Navbar from './NavBar.svelte';
	import Button from './Button.svelte';
	import Gmail from 'svelte-simples/Gmail.svelte';
	import Tooltip from './Tooltip.svelte';
	// import { beforeNavigate } from '$app/navigation';
	import { page } from '$app/stores';
	import Modal from './Modal.svelte';
	import { onMount } from 'svelte';
	import { customBackground } from '$lib/stores/website';
	// import routes from '$lib/NavRoutes';

	export let data;

	let copied = false;

	interface CssVariables {
		[name: string]: string;
	}

	const cssVariables = (
		node: HTMLElement,
		variables: CssVariables
	): { update: (variables: CssVariables) => void } => {
		setCssVariables(node, variables);

		return {
			update(variables: CssVariables) {
				setCssVariables(node, variables);
			}
		};
	};

	const setCssVariables = (node: HTMLElement, variables: CssVariables): void => {
		for (const name in variables) {
			node.style.setProperty(`--${name}`, variables[name]);
		}
	};

	const copy = () => {
		navigator.clipboard.writeText(data.email);
	};

	onMount(() => {
		document.body.style.backgroundImage = `url(${data.image_url})`;
		document.body.style.backgroundSize = 'cover';
		document.body.style.backgroundPosition = 'center';
		document.body.style.backgroundRepeat = 'no-repeat';
	});

	// beforeNavigate(({ to }) => {
	// 	const pathName = to.pathname;
	// 	const route = routes.find((route) => pathName === route.href);
	// 	if (!route.customColor) {
	// 		customBackground.set('#0a0908');
	// 	} else customBackground.set(route.customColor);
	// });
</script>

<svelte:body use:cssVariables={{ background: $customBackground }} />

<Modal>
	<div slot="content" class="modalContainer">
		<h1>Email:</h1>
		<div>
			<p>{data.email}</p>
			&nbsp;
			<div class="tooltip">
				<Tooltip tooltip={copied ? 'Copied' : 'Copy'}>
					<div
						id="clipboard"
						role="button"
						tabindex="0"
						on:keypress={() => {
							copied = true;
							copy();
							setTimeout(() => {
								copied = false;
							}, 500);
						}}
						on:click={() => {
							copied = true;
							copy();
							setTimeout(() => {
								copied = false;
							}, 500);
						}}
					>
						<div>
							<Gmail />
						</div>
					</div>
				</Tooltip>
			</div>
		</div>
		<Button email={data.email}>Send Email</Button>
	</div>
</Modal>

<div class="app">
	<Navbar {data} segment={$page.url.pathname} />
	<main>
		<slot />
	</main>
	<footer class="text-center">
		<div class="pb-8 text-sm text-white">
			Made with ❤️ by <a style="color: #ff3e00;" href="https://epsilon.fm">EpsilonFM</a>
		</div>
	</footer>
</div>

<style>
	* {
		box-sizing: border-box;
	}

	@font-face {
		font-family: 'Fira Code', monospace;
		font-display: optional;
		src: url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;600;700&display=swap');
	}

	:global(#svelte) {
		width: 100vw;
		height: 100%;
		max-width: 900px;

		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}

	:global(html),
	:global(body) {
		transition: background-color 0.2s ease 0s;
		position: relative;
		width: 100%;
		height: 100%;
		overflow: auto;
		font-family: 'Fira Code', monospace;
	}

	:global(body) {
		background-size: 200% 200%;
		color: white;
		margin: 0;
		box-sizing: border-box;
		line-height: 1.75;
		place-items: center;
		height: 100%;
		overflow-x: hidden;
	}

	:global(h1) {
		border: 0;
	}

	:global(::selection) {
		color: white;
		background: #ca3c25;
	}

	:global(::-webkit-scrollbar) {
		width: 8px;
		height: 8px;
		border-radius: 1px;
	}

	:global(::-webkit-scrollbar-thumb) {
		background-color: #fafffd;
		border-radius: 3px;
	}

	:global(::-webkit-scrollbar-track) {
		background-color: transparent;
		border-radius: 1px;
	}

	:global(a) {
		text-decoration: none;
	}

	:global(a) {
		text-decoration: none;
	}

	a {
		color: rgb(0, 100, 200);
		text-decoration: none;
	}

	a:hover {
		text-decoration: underline;
	}

	a:visited {
		color: rgb(0, 80, 160);
	}

	.modalContainer div {
		display: flex;
		margin-bottom: 20px;
	}

	.modalContainer p {
		margin: 0;
	}

	:global(.tooltip) {
		visibility: hidden;
	}
</style>
