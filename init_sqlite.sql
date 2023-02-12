/*
 Navicat Premium Data Transfer

 Source Server         : data
 Source Server Type    : SQLite
 Source Server Version : 3035005 (3.35.5)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3035005 (3.35.5)
 File Encoding         : 65001

 Date: 18/11/2022 14:08:10
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for mailbox
-- ----------------------------
DROP TABLE IF EXISTS "mailbox";
CREATE TABLE "mailbox" (
  "id" integer NOT NULL,
  "name" text(255),
  "email" text(255) NOT NULL,
  "subject" text(255) NOT NULL,
  "phone" text(255),
  "message" text NOT NULL,
  PRIMARY KEY ("id")
);

PRAGMA foreign_keys = true;
