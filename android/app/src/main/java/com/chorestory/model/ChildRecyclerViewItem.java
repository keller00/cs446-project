package com.chorestory.model;

import com.chorestory.R;

import java.util.ArrayList;
import java.util.List;

public class ChildRecyclerViewItem {

    private String name;
    private int imageId;
    private int level;
    private int exp;
    private int quest;

    public static List<ChildRecyclerViewItem> getData() {
        List<ChildRecyclerViewItem> dataList = new ArrayList<>(); // TODO: sort decreasing exp
        String[] names = retrieveNames();
        int[] imageIds = retrieveImages();
        int[] levels = retrieveLevels();
        int[] exps = retrieveExps();
        int[] quests = retrieveQuests();

        for (int i = 0; i < names.length; ++i) {
            ChildRecyclerViewItem item = new ChildRecyclerViewItem();
            item.name = names[i];
            item.imageId = imageIds[i];
            item.level = levels[i];
            item.exp = exps[i];
            item.quest = quests[i];
            dataList.add(item);
        }
        return dataList;
    }

    private static int[] retrieveImages() { // TODO: retrieve images
        return new int[]{
                R.drawable.joker_color,
                R.drawable.soldier_color,
                R.drawable.joker_color,
                R.drawable.knight_color,
                R.drawable.soldier_color,
                R.drawable.knight_color};
    }

    private static String[] retrieveNames() { // TODO: retrieve names
        return new String[]{
                "Christian",
                "Mark",
                "Jim",
                "Isabelle",
                "Minnie",
                "Amanda"
        };
    }

    private static int[] retrieveLevels() { // TODO: retrieve levels
        return new int[]{
                10, 9, 4, 4, 2, 1
        };
    }

    private static int[] retrieveExps() { // TODO: retrieve exps
        return new int[]{
                1021, 919, 442, 400, 200, 12
        };
    }

    private static int[] retrieveQuests() {
        return new int[]{
                200, 100, 42, 40, 20, 1
        };
    }

    public String getName() {
        return name;
    }

    public int getImageId() {
        return imageId;
    }

    public int getLevel() {
        return level;
    }

    public int getExp() {
        return exp;
    }

    public int getQuest() {
        return quest;
    }
}
