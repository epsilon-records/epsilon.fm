export default {
	'*.{ts,js,svelte,css,html}(x)': [
		'prettier --write --list-different',
		() => 'prettier --check',
		'eslint'
	],
	'backend/**/*.py': [
		'poetry --directory ./backend run ruff check --fix',
		'poetry --directory ./backend run ruff format'
	]
};
