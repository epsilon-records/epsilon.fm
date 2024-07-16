module.exports = {
	extends: ['@commitlint/config-conventional'],
	rules: {
		'type-enum': [
			2,
			'always',
			[
				'feat', // ✨   :feat:          feat: a new feature
				'fix', // 🐛   :fix:           fix: a bug fix
				'docs', // 📚️   :docs:          docs: documentation only changes
				'style', // 🎨   :style:         style: changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
				'refactor', // ♻️   :refactor:      refactor: a code change that neither fixes a bug nor adds a feature
				'perf', // ⚡️   :perf:          perf: a code change that improves performance
				'test', // 🚨   :test:          test: adding missing or correcting existing tests
				'chore', // 🔧   :chore:         chore: changes to the build process or auxiliary tools and libraries such as documentation generation
				'chore-release', // 🚀   :chore-release: chore(release): code deployment or publishing to external repositories
				'chore-deps', // 🔗   :chore-deps:    chore(deps): add or delete dependencies
				'build', // 📦️   :build:         build: changes related to build processes
				'ci', // 👷   :ci:            ci: updates to the continuous integration system
				'release', // 🚀   :release:       code deployment or publishing to external repositories
				'security', // 🔒️   :security:      Fixing security issues
				'i18n', // 🌐   :i18n:          Internationalization and localization
				'breaking', // 💥   :breaking:      Introducing breaking changes
				'config', // ⚙️   :config:        Changing configuration files
				'add', // ➕   :add:           add something
				'remove' // ➖   :remove:        remove something
			]
		]
	}
};
