-- This file simply bootstraps the installation of Lazy.nvim and then calls other files for execution
-- This file doesn't necessarily need to be touched, BE CAUTIOUS editing this file and proceed at your own risk.
local lazypath = vim.env.LAZY or vim.fn.stdpath "data" .. "/lazy/lazy.nvim"
local vim = vim
if not (vim.env.LAZY or (vim.uv or vim.loop).fs_stat(lazypath)) then
  -- stylua: ignore
  vim.fn.system({ "git", "clone", "--filter=blob:none", "https://github.com/folke/lazy.nvim.git", "--branch=stable", lazypath })
end
vim.opt.rtp:prepend(lazypath)

-- validate that lazy is available
if not pcall(require, "lazy") then
  -- stylua: ignore
  vim.api.nvim_echo({ { ("Unable to load lazy from: %s\n"):format(lazypath), "ErrorMsg" }, { "Press any key to exit...", "MoreMsg" } }, true, {})
  vim.fn.getchar()
  vim.cmd.quit()
end

local function map(mode, lhs, rhs, opts)
    vim.keymap.set(mode, lhs, rhs, opts)
end

map("n", "<F3>", ":Telescope current_buffer_fuzzy_find<CR>", {desc = "Find Word in a file"}) 
map("n", "<F2>", ":Telescope fd<CR>", {desc = "Find Files"})
map("n", "<F4>", ":LspRestart<CR>", {desc = "Reload Lsp for new libraries"})

vim.api.nvim_set_keymap('n', '<S-Tab>', ':bprev<CR>', { noremap = true })
vim.api.nvim_set_keymap('n', '<Tab>', ':bnext<CR>', { noremap = true })
vim.api.nvim_set_keymap('n', 'd', '"_d', { noremap = true, silent = true })


require "lazy_setup"
require "polish"
